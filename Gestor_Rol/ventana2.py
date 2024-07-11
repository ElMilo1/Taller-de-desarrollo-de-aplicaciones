import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VENTANA PRINCIPAL")
        self.root.geometry("300x200")

        self.button = tk.Button(root, text="Actualizar", command=self.update_label)
        self.button.grid(row=1,columnspan=2,pady=5, padx=5)
        self.button = tk.Button(root, text="Actualizar", command=self.update_label)
        self.button.grid(row=2,columnspan=2,pady=5, padx=5)
        self.button = tk.Button(root, text="Actualizar", command=self.update_label)
        self.button.grid(row=3,columnspan=2,pady=5, padx=5)
        self.button = tk.Button(root, text="Actualizar", command=self.update_label)
        self.button.grid(row=4,columnspan=2,pady=5, padx=5)

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