# import library
import tkinter as tk
from tkinter import messagebox

# Define function for task add
def add_task():
    task=entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        messagebox.showwarning("please enter the task")
    
# Define function for delete a task
def delete_task():
    task=listbox.curselection()
    if task:
        listbox.delete(task)
    else:
        messagebox.showwarning("please selest the task")

# Define function for clear list box
def clearall():
    listbox.delete(0,tk.END)

# Define function for edit task
def edit_task():
    task=listbox.curselection()
    if task:
        listbox.delete(task)
        newtask=entry.get()
        listbox.insert(task,newtask)

# main function
# create a parent window
window=tk.Tk()
window.title("To Do List")

# Create a frame 
frame=tk.Frame(window)
frame.pack(pady=10)

# Add button for task add
button=tk.Button(frame,text="Add Task",font=20,command=add_task)
button.pack(padx=5,side=tk.RIGHT)

# Add entry for user input
entry=tk.Entry(frame,width=50)
entry.pack(padx=5,side=tk.LEFT)

# Add button for delete task
button=tk.Button(text="Delete",font=20,command=delete_task)
button.pack(padx=15,pady=10)

# Add button for delete task
button=tk.Button(text="EDIT",font=20,command=edit_task)
button.pack(padx=15,pady=10)

# Add button for clear all task
button=tk.Button(text="Clear All",font=20,command=clearall)
button.pack(padx=15,pady=5)

# Create a list box 
listbox=tk.Listbox(height=15,width=50)
listbox.pack(pady=5)

window.mainloop()

