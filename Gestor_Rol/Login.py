import tkinter as tk
from tkinter import messagebox
from DAO import DAO



def Login():
    d = DAO()
    user = entry_user.get()
    pwd = entry_pass.get()

    x = d.recCredenciales(user,pwd)
    if x.get_Usuario != None and x.get_Contrasena != None:
        messagebox.showinfo("Ingreso exitoso.")
    else:
        messagebox.showerror("Credenciales incorrectas.")

root = tk.Tk()
root.title("Login")

label_user = tk.Label(root, text = "Usuario")
label_user.pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)

label_pwd = tk.Label(root, text = "Contraseña")
label_pwd.pack(pady=5)
entry_pass = tk.Entry(root)
entry_pass.pack(pady=5)

btn_login = tk.Button(root,text="Ingreso" ,command=Login)
btn_login.pack(pady=5)    
    


root.mainloop()