class Credencial():
    def __init__(self,Usuario,Contrasena,Clase):
        self.__Usuario = Usuario
        self.__Contrasena = Contrasena
        self.__Clase = Clase

    def set_Usuario(self,Usuario):
        self.__Usuario = Usuario
    def set_Contrasena(self,Contrasena):
        self.__Contrasena = Contrasena
    def set_Clase(self,Clase):
        self.__Clase = Clase

    def get_Usuario(self):
        return self.__Usuario
    def get_Contrasena(self):
        return self.__Contrasena
    def get_Clase(self):
        return self.__Clase
        
    def __str__(self):
        txt = f"User: {self.__Usuario}"
        txt += f"\n Pass: {self.__Contrasena}"
        txt += f"\n Clase: {self.__Clase}"
        return txt