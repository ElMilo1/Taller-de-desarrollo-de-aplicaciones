class Personaje():
    def __init__(self,Nombre,Nombre_Usuario,Nivel,Habilidad_ID,Raza_ID,Poder_ID,Equipo1_ID,Equipo2_ID,Equipo3_ID,Equipo4_ID,Equipo5_ID,Estado_ID):
        self.__Nombre = Nombre
        self.__Nombre_Usuario = Nombre_Usuario
        self.__Nivel = Nivel
        self.__Habilidad_ID = Habilidad_ID
        self.__Raza_ID = Raza_ID
        self.__Poder_ID = Poder_ID
        self.__Equipo1_ID = Equipo1_ID
        self.__Equipo2_ID = Equipo2_ID
        self.__Equipo3_ID = Equipo3_ID
        self.__Equipo4_ID = Equipo4_ID
        self.__Equipo5_ID = Equipo5_ID
        self.__Estado_ID = Estado_ID

    def set_Nombre(self,Nombre):
        self.__Nombre = Nombre
    def set_Nombre_Usuario(self,Nombre_Usuario):
        self.__Nombre_Usuario = Nombre_Usuario
    def set_Nivel(self,Nivel):
        self.__Nivel = Nivel
    def set_Habilidad_ID(self,Habilidad_ID):
        self.__Habilidad_ID = Habilidad_ID
    def set_Raza_ID(self,Raza_ID):
        self.__Raza_ID = Raza_ID
    def set_Poder_ID(self,Poder_ID):
        self.__Poder_ID = Poder_ID
    def set_Equipo1_ID(self,Equipo1_ID):
        self.__Equipo1_ID = Equipo1_ID
    def set_Equipo2_ID(self,Equipo2_ID):
        self.__Equipo2_ID = Equipo2_ID
    def set_Equipo3_ID(self,Equipo3_ID):
        self.__Equipo3_ID = Equipo3_ID
    def set_Equipo4_ID(self,Equipo4_ID):
        self.__Equipo4_ID = Equipo4_ID
    def set_Equipo5_ID(self,Equipo5_ID):
        self.__Equipo5_ID = Equipo5_ID
    def set_Estado_ID(self,Estado_ID):
        self.__Estado_ID = Estado_ID

    def get_Nombre(self):
        return self.__Nombre
    def get_Nombre_Usuario(self):
        return self.__Nombre_Usuario
    def get_Nivel(self):
        return self.__Nivel
    def get_Habilidad_ID(self):
        return self.__Habilidad_ID
    def get_Raza_ID(self):
        return self.__Raza_ID
    def get_Poder_ID(self):
        return self.__Poder_ID
    def get_Equipo1_ID(self):
        return self.__Equipo1_ID
    def get_Equipo2_ID(self):
        return self.__Equipo2_ID
    def get_Equipo3_ID(self):
        return self.__Equipo3_ID
    def get_Equipo4_ID(self):
        return self.__Equipo4_ID
    def get_Equipo5_ID(self):
        return self.__Equipo5_ID
    def get_Estado_ID(self):
        self.__Estado_ID

    def __str__(self):
        txt = f" Nombre: {self.__Nombre}"
        txt += f"\n Nombre de usuario: {self.__Nombre_Usuario}"
        txt += f"\n Nivel: {self.__Nivel}"
        txt += f"\n Habilidad ID: {self.__Habilidad_ID}"
        txt += f"\n Raza ID: {self.__Raza_ID}"
        txt += f"\n Poder ID: {self.__Poder_ID}"
        txt += f"\n Equipo 1 ID: {self.__Equipo1_ID}"
        txt += f"\n Equipo 2 ID: {self.__Equipo2_ID}"
        txt += f"\n Equipo 3 ID: {self.__Equipo3_ID}"
        txt += f"\n Equipo 4 ID: {self.__Equipo4_ID}"
        txt += f"\n Equipo 5 ID: {self.__Equipo5_ID}"
        txt += f"\n Estado de personaje: {self.__Estado_ID}"
        return txt