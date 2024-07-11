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
    
    def recCredenciales(self,User,Pwd):
        self.__conectar()
        sql = "SELECT * FROM Credenciales WHERE Usuario = %s AND Contrasena = %s"
        value = (User,Pwd)
        self.__cursor.execute(sql,value)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
<<<<<<< Updated upstream
            x = Credencial(respuesta[0],respuesta[1])
            return x
        else:
            return None
=======
            x = Credencial(respuesta[0],respuesta[1],respuesta[2],respuesta[3])
            return x
        else:
            return None
        
        # Registro de usuario, y previo al registro de datos, realiza una query de busqueda donde, al encontrar los datos guardados, retorna 1 comprobando que se realizo el registro con exito
    def regCredenciales(self,User:Credencial):
        self.__conectar()
        sql = "INSERT INTO `Credenciales`(`Usuario`, `Contrasena`, `Clase`) VALUES (%s,%s,%s)"
        values = (User.get_Usuario,User.get_Contrasena,User.get_Clase)
        self.__cursor.execute(sql,values)
        sql2 = "SELECT Usuario , Contrasena FROM Credenciales WHERE Usuario == %s AND Contrasena == %s"
        self.__cursor.execute(sql2)
        respuesta = self.__cursor.fetchone()
        self.__cerrar()
        if respuesta != None:
            return 1
        else:
            return None
        
    def regRaza(self,Nombre):
        self.__conectar()
        sql = "INSERT INTO Raza('Nombre) VALUE %s"
        value = (Nombre,)
        self.__cursor.execute(sql,value)
        respuesta = self.__
>>>>>>> Stashed changes
