class Equipamiento():
    def __init__(self,Equipo_ID,Nombre,Tipo_Equipamiento,Estado):
        self.__Equipo_Id = Equipo_ID
        self.__Nombre = Nombre
        self.__Tipo_Equipamiento = Tipo_Equipamiento
        self.__Estado = Estado

    def set_Equipo_ID(self,Equipo_ID):
        self.__Equipo_Id = Equipo_ID
    def set_Nombre(self,Nombre):
        self.__Nombre = Nombre
    def set_Tipo_Equipamiento(self,Tipo_Equipamiento):
        self.__Tipo_Equipamiento = Tipo_Equipamiento
    def set_Estado(self,Estado):
        self.__Estado = Estado

    def get_Equipo_ID(self):
        return self.__Equipo_Id
    def get_Nombre(self):
        return self.__Nombre
    def get_Tipo_Equipamiento(self):
        return self.__Tipo_Equipamiento
    def get_Estado(self):
        return self.__Estado
    
    def __str__(self):
        txt = f" Equipo_ID: {self.__Equipo_Id}"
        txt += f"\n Nombre equipo: {self.__Nombre}"
        txt += f"\n Tipo equipamiento: {self.__Tipo_Equipamiento}"
        if self.__Estado == "Disponible":
            txt += f"\n Estado: Disponible."
        else:
            txt += f"\n Estado: No disponible."
        return txt