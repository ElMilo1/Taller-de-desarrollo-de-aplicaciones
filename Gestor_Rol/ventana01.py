#INICIAR SESION
import tkinter as tk
from tkinter import messagebox
import ventana02
import ventana03
import ventana05
from DAO import DAO

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("INICIO DE SESION")
        self.root.resizable(0,0)
        window_width = 210
        window_height = 130

        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular la posición del centro
        position_top = int((screen_height / 2) - (window_height / 2))
        position_right = int((screen_width / 2) - (window_width / 2))

        # Establecer la geometría de la ventana
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.label = tk.Label(root, text="Nombre")
        self.label.grid(row=0,column=0,padx=5,pady=5)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0,column=1,padx=5,pady=5)

        self.label2 = tk.Label(root, text="Contraseña")
        self.label2.grid(row=1,column=0,padx=5,pady=5)

        self.entry2 = tk.Entry(root,show="*")
        self.entry2.grid(row=1,column=1,padx=5,pady=5)

        self.button = tk.Button(root, text="Iniciar sesion", command=self.update_label)
        self.button.grid(row=2,columnspan=2,pady=0)

        self.button = tk.Button(root, text="Registrar", command=self.registrar)
        self.button.grid(row=3,columnspan=2,pady=0)

    def update_label(self):
        d = DAO()
        user = self.entry.get()
        pwd = self.entry2.get()

        x = d.recCredenciales(user,pwd)
        try:
            if x.get_Usuario != None and x.get_Contrasena != None:
                if x.get_Clase() != "GM":
                    messagebox.showinfo("Inicio de sesion.", "Inicio de sesion exitoso.")
                    self.root.withdraw()
                    ventana02.ventana2()
                    
                elif x.get_Clase() =="GM":
                    messagebox.showinfo("Inicio de sesion.", "Inicio de sesion exitoso.")
                    self.root.withdraw()
                    ventana05.main()
                else:
                    messagebox.showinfo("Error","A ocurrido un error.")
            else:
                messagebox.showinfo("Error","Nombre de usuario o contraseña incorrectos.")
        except:
            messagebox.showinfo("Error","Nombre de usuario o contraseña incorrectos.")
    def registrar(self):
        self.root.withdraw()
        ventana03.main()

    #def set_label_text(self, text):
        # Actualizar el texto del Label
        #self.label.config(text=text)
def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
