#REGISTRAR USUARIO
import tkinter as tk
from tkinter import messagebox
import ventana01
from Credencial import Credencial
from DAO import DAO

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CREA TU CUENTA")
        self.root.resizable(0,0)
        window_width = 210
        window_height = 150

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular la posición del centro
        position_top = int((screen_height / 2) - (window_height / 2))
        position_right = int((screen_width / 2) - (window_width / 2))

        # Establecer la geometría de la ventana
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

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
        d = DAO()
        d.regCredenciales(usuario)
        messagebox.showinfo("Registro.", "Registro exitoso.")
        self.root.withdraw()
        ventana01.main()


    def cancelar(self):
        self.root.withdraw()
        ventana01.main()

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
