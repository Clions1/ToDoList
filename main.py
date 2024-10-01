import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.geometry("500x400")
window.resizable(False, False)


def add_task():
    if len(task_list) >= 10:
        messagebox.showwarning("Warning", "You can add a maximum of 10 tasks.")
    else:
        task = task_entry.get("1.0", tk.END).strip()
        if task:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(task_frame, text=task, variable=var)
            checkbox.var = var
            checkbox.pack(anchor='w')
            task_list.append((checkbox, var))
            task_entry.delete("1.0", tk.END)


def complete_task():
    for checkbox, var in task_list[:]:
        if var.get() == 1:
            checkbox.destroy()
            task_list.remove((checkbox, var))


title_label = tk.Label(window, text="Write down the tasks you want to plan", font=("bold"))
title_label.pack()


task_entry = tk.Text(window, height=1, width=20)
task_entry.place(x=60, y=50)


add_button = tk.Button(window, text="Ekle", height=2, width=8, command=add_task)
add_button.place(x=110, y=85)


task_frame = tk.Frame(window, width=150, height=250)
task_frame.place(x=322, y=30)
task_frame.grid_propagate(False)


complete_button = tk.Button(window, text="Tamamla", height=2, width=8, command=complete_task)
complete_button.place(x=340, y=300)


task_list = []


window.mainloop()
