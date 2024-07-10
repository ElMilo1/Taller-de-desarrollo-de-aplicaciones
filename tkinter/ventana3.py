import tkinter as tk
from tkinter import messagebox
import ventana1
from Gestor_Rol import Credencial
from Gestor_Rol import DAO

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("INICIO DE SESION")
        self.root.geometry("210x150")

        self.label = tk.Label(root, text="Nombre:")
        self.label.grid(row=0,column=0,padx=5,pady=5)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0,column=1,padx=5,pady=5)

        self.label2 = tk.Label(root, text="Contraseña")
        self.label2.grid(row=1,column=0,padx=5,pady=5)

        self.entry2 = tk.Entry(root,show="*")
        self.entry2.grid(row=1,column=1,padx=5,pady=5)

        self.radio = tk.IntVar()

        self.usuario = tk.Radiobutton(root,text ="Usuario",value=1, variable=self.radio)
        self.usuario.grid(row=2,column=0,padx=5,pady=5)

        self.gamemaster = tk.Radiobutton(root,text ="Game Master",value=2, variable=self.radio)
        self.gamemaster.grid(row=2,column=1,padx=5,pady=5)


        self.button = tk.Button(root, text="Registrar", command=self.registrar)
        self.button.grid(row=3,columnspan=2,pady=0)

        self.button = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.button.grid(row=4,columnspan=2,pady=0)


    def registrar(self):
        nombre = self.entry.get().capitalize()
        contrasena = self.entry2.get()
        clase = self.radio.get()
        if clase == 1:
            clase = "Usuario"
        else:
            clase = "GM"

        usuario = Credencial(nombre,contrasena,clase)


    def cancelar(self):
        self.root.withdraw()
        ventana1.main()




def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
