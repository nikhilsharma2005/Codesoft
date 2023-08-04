import random
import string
import tkinter as tk
from tkinter import messagebox

#Password Generator password
def generate_random_password():
    characters = string.ascii_letters
    characters += string.digits
    characters += string.punctuation
    length=int(length_var.get())
    if length:
        password = ''.join(random.choice(characters) for _ in range(length))
    else:
        messagebox.showwarning("please enter length")
    password_var.set(password)

#Reset function
def reset():
    user_var.set("")
    password_var.set("")
    length_var.set("")

#Accept function
def accept():
    wk.destroy()

wk=tk.Tk()
wk.title("Random Password Genertor")
wk.geometry("500x400")

label=tk.Label(wk,text="Password Genetator",font=25,fg="blue")
label.pack(pady=20)

frame1=tk.Frame(wk)
frame1.pack(pady=16)

frame2=tk.Frame(wk)
frame2.pack(pady=14)

frame3=tk.Frame(wk)
frame3.pack(pady=12)

user_label=tk.Label(frame1,text="Enter user name :")
user_label.pack(side="left")

length_label=tk.Label(frame2,text="Enter Password Length :")
length_label.pack(side="left")

generate_label=tk.Label(frame3,text="Generate Password:")
generate_label.pack(side="left")

user_var=tk.StringVar()
user_entry=tk.Entry(frame1,textvariable=user_var)
user_entry.pack(side="right")

length_var = tk.IntVar()
length_entry=tk.Entry(frame2,textvariable=length_var)
length_entry.pack(side="right")

password_var = tk.StringVar()
generate_entry=tk.Entry(frame3,bg="white",textvariable=password_var, state="readonly")
generate_entry.pack(side="right")

generate_button=tk.Button(wk,text="Generate Password",bg="blue",fg="white",font=20,command=generate_random_password)
generate_button.pack(pady=9)

accept_button=tk.Button(wk,text="Accept",font=15,command=accept)
accept_button.pack(pady=7)

reset_button=tk.Button(wk,text="Reset",font=15,command=reset)
reset_button.pack(pady=5)



wk.mainloop()