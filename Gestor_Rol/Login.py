import tkinter as tk
from tkinter import messagebox
from DAO import DAO
from tkinter import ttk

def Login():
    d = DAO()
    user = ""
    pwd = ""
    user = entry_user.get()
    pwd = entry_pass.get()

    x = d.recCredenciales(user,pwd)
    if x.get_Usuario != None and x.get_Contrasena != None:
        messagebox.showinfo("Login","Ingreso exitoso.")
    elif x.get_Usuario == None or x.get_Contrasena == None:
        messagebox.showinfo("Credenciales incorrectas.")

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

label_user = tk.Label(root, text = "Ingrese su nombre de usuario:")
label_user.pack(pady=10)
entry_user = tk.Entry(root)
entry_user.pack(pady=10)

label_pwd = tk.Label(root, text = "Ingrese su contraseña:")
label_pwd.pack(pady=5)
entry_pass = tk.Entry(root)
entry_pass.pack(pady=5)

btn_login = tk.Button(root,text="Ingreso" ,command=Login)
btn_login.pack(pady=5)    
    


root.mainloop()