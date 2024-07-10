class Raza():
    def __init__(self,Raza_ID,Nombre):
        self.__Raza_ID = Raza_ID
        self.__Nombre = Nombre

    def set_Raza_ID(self,Raza_ID):
        self.__Raza_ID = Raza_ID
    def set_Nombre(self,Nombre):
        self.__Nombre = Nombre

    def get_Raza_ID(self):
        return self.__Raza_ID
    def get_Nombre(self):
        return self.__Nombre
    
    def __str__(self):
        txt = f" Raza ID: {self.__Raza_ID}"
        txt += f"\n Nombre: {self.__Nombre}"
        return txt