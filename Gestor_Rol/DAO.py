import mysql.connector
import Credenciales
from Equipamiento import Equipamiento
from Personaje import Personaje
from Poder import Poder
from Estado import Estado
from Habilidad  import Habilidad
from Raza import Raza
from Credencial import Credencial

class DAO():
    def __init__(self):
        pass
    def __conectar(self):
        self.__conexion = mysql.connector.connect(**Credenciales.get_Credenciales())
        self.__cursor = self.__conexion.cursor()

    def __cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    # Recuperacion de toda la tabla raza
    def recDetRaza(self):
        self.__conectar()
        sql = "SELECT * FROM Raza"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        lista = []
        for i in respuesta:
            x = Raza(i[0],i[1])
            lista.append(x)
        self.__cerrar()
        return lista

    # Recuperacion de la tabla Raza, mostrando su id y nombre
    def recRaza(self,Raza_ID):
        self.__conectar()
        sql = "SELECT * FROM Raza WHERE RazaID = %s"
        value = (Raza_ID,)
        self.__cursor.execute(sql,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            x = Raza(respuesta[0],respuesta[1])
            return x
        else:
            return None

    # Recuperacion de la tabla Poder, mostrando su nombre, id, raza perteneciente y descripcion    
    def recPoder(self,Raza_ID):
        self.__conectar()
        sql ="SELECT * FROM Poder WHERE RazaID = %s"
        value = (Raza_ID,)
        self.__cursor.execute(sql,value)
        respuesta = self.__cursor.fetchall()
        lista = []
        for i in respuesta:
            x = Poder(i[0],i[1],i[2],i[3],i[4])
            lista.append(x)
        self.__cerrar()
        return lista
    
    # Recuperacion de la tabla Habilidad, mostrando su nombre, id, raza perteneciente y descripcion    
    def recHabilidad(self,Raza_ID):
        self.__conectar()
        sql = "SELECT * FROM Habilidad WHERE RazaID = %s"
        value = (Raza_ID,)
        self.__cursor.execute(sql,value)
        respuesta = self.__cursor.fetchall()
        lista = []
        for i in respuesta:
            x = Habilidad(i[0],i[1],i[2],i[3],i[4])
            lista.append(x)
        self.__cerrar()
        return lista
    
    # Recuperacion de la tabla Equipo, mostrando su nombre, id y tipo de equipo
    def recEquipo(self,Tipo_Equipo):
        self.__conectar()
        sql = "SELECT * FROM Equipamiento WHERE Tipo_Equipamiento = %s"
        value = (Tipo_Equipo,)
        self.__cursor.execute(sql,value)
        respuesta = self.cursor.fetchall()
        lista = []
        for i in respuesta:
            x = Equipamiento(i[0],i[1],i[2],i[3])
            lista.append(x)
        self.__cerrar()
        return lista
    
    # recuperacion de la tabla Estado, mostrando su nombre, id, descripcion y efecto
    def recEstado(self):
        self.__conectar()
        sql = "SELECT * FROM Estado"
        self.__cursor.execute(sql)
        respuesta = self.__cursor.fetchall()
        lista = []
        for i in respuesta:
            x = Estado(i[0],i[1],i[2],i[3])
            lista.append(x)
        self.__cerrar()
        return lista
    
    # Recuperacion de credenciales, cotejadas en el login para poder acceder a la aplicacion
    def recCredenciales(self,User,Pwd):
        self.__conectar()
        sql = "SELECT * FROM Credenciales WHERE Usuario = %s AND Contrasena = %s"
        value = (User,Pwd)
        self.__cursor.execute(sql,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            x = Credencial(respuesta[0],respuesta[1],respuesta[2])
            return x
        else:
            return None
        
        # Registro de usuario, y previo al registro de datos, realiza una query de busqueda donde, al encontrar los datos guardados, retorna 1 comprobando que se realizo el registro con exito
    def regCredenciales(self,User:Credencial):
        self.__conectar()
        sql = "INSERT INTO `Credenciales`(`Usuario`, `Contrasena`, `Clase`) VALUES (%s,%s,%s)"
        values = (User.get_Usuario(),User.get_Contrasena(),User.get_Clase())
        self.__cursor.execute(sql,values)
        sql2 = "SELECT Usuario , Contrasena FROM Credenciales WHERE Usuario = '%s' AND Contrasena = '%s'"
        self.__cursor.execute(sql2)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None
        
        # Registro de Nueva raza, solo se recibe y envia nombre ya que el ID es autoincrementable en la base de datos.
    def regRaza(self,Nombre):
        self.__conectar()
        sql = "INSERT INTO Raza('Nombre') VALUE %s"
        value = (Nombre,)
        self.__cursor.execute(sql,value)
        sql2 = "SELECT * FROM Raza WHERE Nombre = %s"
        self.__cursor.execute(sql2)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None
        
        # Registro de nuevo poder, recibiendo nombre, id de raza correspondiente y descripcion, resto de datos se aplican en la base de datos
    def regPoder(self,Raza_ID,Nombre_Poder,Descripcion):
        self.__conectar()
        sql = "INSERT INTO 'Poder'('RazaID','Nombre_Poder','Descripcion') VALUES %s ,%s, %s"
        values = (Raza_ID,Nombre_Poder,Descripcion)
        self.__cursor.execute(sql,values)
        sql2 = "SELECT* FROM 'Poder' WHERE 'Nombre_Poder' = %s"
        value = (Nombre_Poder,)
        self.__cursor.execute(sql2,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None
        
        # Registro de nueva habilidad, recibiendo nombre, id de raza correspondiente y descripcion, resto de datos se aplican en la base de datos
    def regHabilidad(self,Raza_ID,Nombre_Habilidad,Descripcion):
        self.__conectar()
        sql = "INSERT INTO 'Habilidad'('RazaID','Nombre_Habilidad','Descripcion') VALUES %s ,%s, %s"
        values = (Raza_ID,Nombre_Habilidad,Descripcion)
        self.__cursor.execute(sql,values)
        sql2 = "SELECT* FROM 'Habilidad' WHERE 'Nombre_Habilidad' = %s"
        value = (Nombre_Habilidad,)
        self.__cursor.execute(sql2,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None
        
        # Registro de nuevo estado, recibiendo nombre, Descripcion y efecto de este, id y estado se aplican en la base de datos
    def regEstado(self,Nombre,Descripcion,Efecto):
        self.__conectar()
        sql = "INSERT INTO 'Estado'('Nombre','Descripcion','Efecto') VALUES %s, %s , %s"
        values = (Nombre,Descripcion,Efecto)
        self.__cursor.execute(sql,values)
        sql2 = "SELECT * FROM 'Estado' WHERE 'Nombre' = %s"
        value = (Nombre,)
        self.__cursor.execute(sql2,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None
        
        # Registro de nuevo equipo, recibiendo nombre y tipo de equipo, ya que estado y Id se aplican en base de datos
    def regEquipo(self,Nombre_Equipo,Tipo_Equipo):
        self.__conectar()
        sql = "INSERT INTO 'Equipamiento'('Nombre_Equipo','Tipo_Equipamiento') VALUES %s, %s"
        values =(Nombre_Equipo,Tipo_Equipo)
        self.__cursor.execute(sql,values)
        sql2 = "SELECT * FROM 'Equipamiento' WHERE 'Nombre_Equipo' = %s"
        value = (Nombre_Equipo,)
        self.__cursor.execute(sql2,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None