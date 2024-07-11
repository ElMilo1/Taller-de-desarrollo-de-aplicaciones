import tkinter as tk
from tkinter import messagebox
import ventana02
from Credencial import Credencial
from DAO import DAO

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crea tu personaje")
        self.root.geometry("210x150")

        self.label = tk.Label(root, text="Nombre:")
        self.label.grid(row=0,column=0,padx=5,pady=5)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0,column=1,padx=5,pady=5)

        self.radio = tk.IntVar()

        self.opciones = ["Humano", "Elfo", "Enano" , "Argoniano"]
        self.seleccion = tk.StringVar()
        self.seleccion.set(self.opciones[0])
        self.menu = tk.OptionMenu(root, self.seleccion, *self.opciones)
        self.menu.grid(row=2,column=1,padx=5,pady=5)


        self.button = tk.Button(root, text="Registrar", command=self.registrar)
        self.button.grid(row=3,columnspan=2,pady=0)

        self.button = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.button.grid(row=4,columnspan=2,pady=0)


    def registrar(self):
        pass

    def cancelar(self):
        self.root.withdraw()
        ventana02.main()

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
