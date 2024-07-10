class Estado():
    def __init__(self,Estado_ID,Nombre,Descripcion,Efecto):
        self.__Estado_ID = Estado_ID
        self.__Nombre = Nombre
        self.__Descripcion = Descripcion
        self.__Efecto = Efecto

    def set_estado(self,Estado_ID):
        self.__Estado_ID = Estado_ID
    def set_nombre(self,Nombre):
        self.__Nombre = Nombre
    def set_Descripcion(self,Descripcion):
        self.__Descripcion = Descripcion
    def set_Efecto(self,Efecto):
        self.__Efecto = Efecto

    def get_Estado_ID(self):
        return self.__Estado_ID
    def get_nombre(self):
        return self.__Nombre
    def get_Descripcion(self):
        return self.__Descripcion
    def get_Efecto(self):
        return self.__Efecto
    
    def __str__(self):
        txt = f" ID: {self.__Estado_ID}"
        txt += f"\n Nombre estado: {self.__Nombre}"
        txt += f"\n Descripcion: {self.__Descripcion}"
        txt += f"\n Efecto {self.__Efecto}"
        return txt