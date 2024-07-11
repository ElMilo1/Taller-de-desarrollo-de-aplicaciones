#PAGINA DE USUARIO
import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VENTANA PRINCIPAL")
        self.root.geometry("300x130")

        self.button1 = tk.Button(root, text="Crear Personaje", command=self.update_label)
        self.button1.grid(row=1,columnspan=2,pady=1, padx=5)
        self.label1 = tk.Label(root, text="Crea tu personaje como tu quieras.")
        self.label1.grid(row=1,column=4,padx=5,pady=5) 
        self.button2 = tk.Button(root, text="Ver Personaje", command=self.update_label)
        self.button2.grid(row=3,columnspan=2,pady=5, padx=5)
        self.label2 = tk.Label(root, text="Ve el estado de tu personaje.")
        self.label2.grid(row=3,column=4,padx=5,pady=5) 
        self.button3 = tk.Button(root, text="Editar Equipo", command=self.update_label)
        self.button3.grid(row=5,columnspan=2,pady=5, padx=5)
        self.label3 = tk.Label(root, text="Edita el equipo de tu personaje.")
        self.label3.grid(row=5,column=4,padx=5,pady=5)

    def update_label(self):
        pass

    #def set_label_text(self, text):
        # Actualizar el texto del Label
        #self.label.config(text=text)
def ventana2():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    ventana2()