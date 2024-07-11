#PAGINA DE USUARIO
import tkinter as tk
from tkinter import messagebox
import ventana04

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VENTANA PRINCIPAL")
        self.root.resizable(0,0)
        window_width = 300
        window_height = 130

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular la posición del centro
        position_top = int((screen_height / 2) - (window_height / 2))
        position_right = int((screen_width / 2) - (window_width / 2))

        # Establecer la geometría de la ventana
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.button1 = tk.Button(root, text="Crear Personaje", command=self.crear_personaje)
        self.button1.grid(row=1,columnspan=2,pady=1, padx=5)
        self.label1 = tk.Label(root, text="Crea tu personaje como tu quieras.")
        self.label1.grid(row=1,column=4,padx=5,pady=5) 
        self.button2 = tk.Button(root, text="Ver Personaje", command=self.ver_personaje)
        self.button2.grid(row=3,columnspan=2,pady=5, padx=5)
        self.label2 = tk.Label(root, text="Ve el estado de tu personaje.")
        self.label2.grid(row=3,column=4,padx=5,pady=5) 
        self.button3 = tk.Button(root, text="Editar Equipo", command=self.editar_equipo)
        self.button3.grid(row=5,columnspan=2,pady=5, padx=5)
        self.label3 = tk.Label(root, text="Edita el equipo de tu personaje.")
        self.label3.grid(row=5,column=4,padx=5,pady=5)

    def crear_personaje(self):
        self.root.withdraw()
        ventana04.main()

    def ver_personaje(self):
        pass

    def editar_equipo():
        pass

def ventana2():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    ventana2()