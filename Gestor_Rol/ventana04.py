import tkinter as tk
from tkinter import messagebox
import ventana02
from Credencial import Credencial
from DAO import DAO
from Raza import Raza

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crea tu personaje")
        self.root.geometry("230x150")

        self.label = tk.Label(root, text="Nombre:")
        self.label.grid(row=0,column=0,padx=5,pady=5)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0,column=1,padx=5,pady=5)


        self.opciones = self.recuperar_raza()
        self.seleccion = tk.StringVar()
        self.seleccion.set(self.opciones[0])

        self.menu = tk.OptionMenu(root, self.seleccion, *self.opciones)
        self.menu.grid(row=1,column=1,padx=5,pady=5)

        self.label_select = tk.Label(root, text=f"raza seleccionada: {self.seleccion.get()}")
        self.label_select.grid(row=2,column=1,padx=4,pady=2)
        self.seleccion.trace("w",self.actualizar_label)

        self.button = tk.Button(root, text="Registrar", command=self.registrar)
        self.button.grid(row=3,columnspan=2,pady=0)

        self.button = tk.Button(root, text="Cancelar", command=self.cancelar)
        self.button.grid(row=4,columnspan=2,pady=0)

    def recuperar_raza(self):
        d = DAO()
        datos = d.recDetRaza()
        opciones = [i.get_Nombre() for i in datos]
        return opciones
    
    def actualizar_label(self, *args):
        self.label_select.config(text=f"Raza seleccionada: {self.seleccion.get()}")

    def registrar(self):
        nombre = self.entry.get()
        raza = self.seleccion.get()

    def cancelar(self):
        self.root.withdraw()
        ventana02.ventana2()

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
