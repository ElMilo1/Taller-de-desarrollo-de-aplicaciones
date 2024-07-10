class Habilidad():
    def __init__(self,Habilidad_ID,Raza_ID,Nombre_habilidad,Descripcion,Estado):
        self.__Habilidad_ID = Habilidad_ID
        self.__Raza_ID = Raza_ID
        self.__Nombre_Habilidad = Nombre_habilidad
        self.__Descripcion = Descripcion
        self.__Estado = Estado

    def set_Habilidad_ID(self,Habilidad_ID):
        self.__Habilidad_ID = Habilidad_ID
    def set_Raza_ID(self,Raza_ID):
        self.__Raza_ID = Raza_ID
    def set_Nombre_Habilidad(self,Nombre_Habilidad):
        self.__Nombre_Habilidad = Nombre_Habilidad
    def set_Descripcion(self,Descripcion):
        self.__Descripcion = Descripcion
    def set_Estado(self,Estado):
        self.__Estado = Estado

    def get_Habilidad_ID(self):
        return self.__Habilidad_ID
    def get_Raza_ID(self):
        return self.__Raza_ID
    def get_Nombre_Habilidad(self):
        return self.__Nombre_Habilidad
    def get_Descripcion(self):
        return self.__Descripcion
    def get_Estado(self):
        return self.__Estado
    
    def __str__(self):
        txt = f" ID: {self.__Habilidad_ID}"
        txt += f"\n Raza ID: {self.__Raza_ID}."
        txt += f"\n Nombre habilidad: {self.__Nombre_Habilidad}."
        txt += f"\n Descripcion: {self.__Descripcion}."
        if self.__Asignado == "Disponible":
            txt += f"\n Estado: Disponible."
        else:
            txt += f"\n Estado: No disponible."
        return txt