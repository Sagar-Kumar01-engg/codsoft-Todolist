from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("644x455")
root.title("Todo-List")

def add_task():
    task = task_init.get()
    if task != "":
        list_box.insert(END, task)
        task_init.delete(0, END)
    else:
        messagebox.showwarning("Wrong", "Enter some word")

def delete_task():
    try:
        selected_index = list_box.curselection()[0]
        list_box.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Wrong", "Select the task")

def clear_all():
    list_box.delete(0, END)

task_init = Entry(root, font="lucida 20 bold")
task_init.pack(fill=X, padx=6, pady=8)

f = Frame(root)
f.pack()

Button(f, text="Save", font="lucida 15 bold", command=add_task).pack(padx=5, pady=10)

list_box = Listbox(root, height=10, font="lucida 14")
list_box.pack(fill=X, padx=5)

Button(root, text="Delete selected", font="lucida 12", command=delete_task).pack(pady=10)
Button(root, text="Clear all", font="lucida 12", command=clear_all).pack()

root.mainloop()