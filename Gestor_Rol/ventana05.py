#Pagina GM
import tkinter as tk
from tkinter import messagebox
import ventana04

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VENTANA PRINCIPAL GM")
        self.root.resizable(0,0)
        window_width = 340
        window_height = 420

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular la posición del centro
        position_top = int((screen_height / 2) - (window_height / 2))
        position_right = int((screen_width / 2) - (window_width / 2))

        # Establecer la geometría de la ventana
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


        self.button1 = tk.Button(root, text="Registrar Raza", command=self.update_label)
        self.button1.grid(row=1,columnspan=2,pady=1, padx=5)
        self.label1 = tk.Label(root, text="Registrar la raza que quieras.")
        self.label1.grid(row=1,column=4,padx=5,pady=5) 
        self.button2 = tk.Button(root, text="Ver Raza", command=self.update_label)
        self.button2.grid(row=2,columnspan=2,pady=5, padx=5)
        self.label2 = tk.Label(root, text="Ve las Razas registradas.")
        self.label2.grid(row=2,column=4,padx=5,pady=5) 
        self.button3 = tk.Button(root, text="Registrar Poder", command=self.update_label)
        self.button3.grid(row=3,columnspan=2,pady=5, padx=5)
        self.label3 = tk.Label(root, text="Registra el poder que quieras.")
        self.label3.grid(row=3,column=4,padx=5,pady=5)
        self.button1 = tk.Button(root, text="Ver Poder", command=self.update_label)
        self.button1.grid(row=4,columnspan=2,pady=1, padx=5)
        self.label1 = tk.Label(root, text="Ve los poderes registrados.")
        self.label1.grid(row=4,column=4,padx=5,pady=5) 
        self.button2 = tk.Button(root, text="Registrar Habilidad", command=self.update_label)
        self.button2.grid(row=5,columnspan=2,pady=5, padx=5)
        self.label2 = tk.Label(root, text="Registra la habilidad que quieras.")
        self.label2.grid(row=5,column=4,padx=5,pady=5) 
        self.button3 = tk.Button(root, text="Ver Habilidad", command=self.update_label)
        self.button3.grid(row=6,columnspan=2,pady=5, padx=5)
        self.label3 = tk.Label(root, text="Ve las habilidades registradas.")
        self.label3.grid(row=6,column=4,padx=5,pady=5)
        self.button1 = tk.Button(root, text="Registrar Estado", command=self.update_label)
        self.button1.grid(row=7,columnspan=2,pady=1, padx=5)
        self.label1 = tk.Label(root, text="Registra el estado del personaje que quieras.")
        self.label1.grid(row=7,column=4,padx=5,pady=5) 
        self.button2 = tk.Button(root, text="Ver Estado", command=self.update_label)
        self.button2.grid(row=8,columnspan=2,pady=5, padx=5)
        self.label2 = tk.Label(root, text="Ve los estados registrados.")
        self.label2.grid(row=8,column=4,padx=5,pady=5) 
        self.button3 = tk.Button(root, text="Registrar Equipo", command=self.update_label)
        self.button3.grid(row=9,columnspan=2,pady=5, padx=5)
        self.label3 = tk.Label(root, text="Registra el equipo que quieras.")
        self.label3.grid(row=9,column=4,padx=5,pady=5)
        self.button1 = tk.Button(root, text="Ver Equipo", command=self.update_label)
        self.button1.grid(row=10,columnspan=2,pady=1, padx=5)
        self.label1 = tk.Label(root, text="Ve el equipo registrado.")
        self.label1.grid(row=10,column=4,padx=5,pady=5) 
        self.button2 = tk.Button(root, text="Editar Personaje", command=self.update_label)
        self.button2.grid(row=11,columnspan=2,pady=5, padx=5)
        self.label2 = tk.Label(root, text="Edita al personaje que quieras.")
        self.label2.grid(row=11,column=4,padx=5,pady=5) 
        self.button3 = tk.Button(root, text="Ver Personaje", command=self.update_label)
        self.button3.grid(row=12,columnspan=2,pady=5, padx=5)
        self.label3 = tk.Label(root, text="Ve el estado del personaje.")
        self.label3.grid(row=12,column=4,padx=5,pady=5)

    def update_label(self):
        pass

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()