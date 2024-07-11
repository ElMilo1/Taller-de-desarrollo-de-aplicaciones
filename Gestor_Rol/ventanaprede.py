import tkinter as tk
from tkinter import messagebox
#import ventana2

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("INICIO DE SESION")
        self.root.geometry("210x100")

        self.label = tk.Label(root, text="Nombre")
        self.label.grid(row=0,column=0,padx=5,pady=5)

        self.entry = tk.Entry(root)
        self.entry.grid(row=0,column=1,padx=5,pady=5)

        self.label2 = tk.Label(root, text="Contraseña")
        self.label2.grid(row=1,column=0,padx=5,pady=5)

        self.entry2 = tk.Entry(root,show="*")
        self.entry2.grid(row=1,column=1,padx=5,pady=5)

        self.button = tk.Button(root, text="Actualizar", command=self.update_label)
        self.button.grid(row=2,columnspan=2,pady=0)

        self.button = tk.Button(root, text="Registrar", command=self.update_label)
        self.button.grid(row=2,columnspan=2,pady=0)

    def update_label(self):
        usuario = self.entry.get()
        contrasena = self.entry2.get()

        if usuario  == "admin" and contrasena =="1234":
            messagebox.showinfo("Inicio de sesion.", "Inicio de sesion exitoso.")
            self.root.withdraw()
           #ventana2.ventana2()

        else:
            messagebox.showinfo("Error","Nombre de usuario o contraseña incorrectos.")

    def registrar(self):
        self.root.withdraw()
       # ventana3.ventana3()

    #def set_label_text(self, text):
        # Actualizar el texto del Label
        #self.label.config(text=text)
def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
