import tkinter as tk
from tkinter import messagebox

tasks = []

# ADD TASK
def add_task():
    task = entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
        return

    var = tk.IntVar()

    cb = tk.Checkbutton(
        task_frame,
        text=task,
        variable=var,
        font=("Arial",12),
        bg="#f0f8ff"
    )

    cb.pack(anchor="w", pady=2)

    tasks.append((var, cb))
    entry.delete(0, tk.END)


# DELETE SELECTED TASK
def delete_task():
    global tasks

    for var, cb in tasks:
        if var.get() == 1:
            cb.destroy()
            tasks.remove((var, cb))
            return

    messagebox.showwarning("Warning", "Select a task to delete")


# MODIFY TASK
def modify_task():

    for var, cb in tasks:
        if var.get() == 1:

            new_task = entry.get()

            if new_task == "":
                messagebox.showwarning("Warning", "Enter modified task")
                return

            cb.config(text=new_task)
            entry.delete(0, tk.END)
            return

    messagebox.showwarning("Warning", "Select a task to modify")


# DISPLAY TASKS
def display_tasks():

    output = ""

    for i,(var,cb) in enumerate(tasks, start=1):

        status = "✔" if var.get() else "☐"  

        output += f"{i}. {status} {cb.cget('text')}\n"

    if output == "":
        output = "No tasks available"

    messagebox.showinfo("Task List", output)


# MAIN WINDOW
root = tk.Tk()
root.title("The To-Do List")
root.geometry("420x480")
root.configure(bg="#d6f5ff")


title = tk.Label(
    root,
    text=" My To-Do List ",
    font=("Arial",18,"bold"),
    bg="#d6f5ff",
    fg="#003366"
)

title.pack(pady=15)


entry = tk.Entry(root, width=30, font=("Arial",12))
entry.pack(pady=10)


btn_frame = tk.Frame(root, bg="#d6f5ff")
btn_frame.pack()


add_btn = tk.Button(
    btn_frame,
    text="Add Task",
    bg="#4CAF50",
    fg="white",
    width=12,
    command=add_task
)

add_btn.grid(row=0,column=0,padx=5,pady=5)


modify_btn = tk.Button(
    btn_frame,
    text="Modify Task",
    bg="#2196F3",
    fg="white",
    width=12,
    command=modify_task
)

modify_btn.grid(row=0,column=1,padx=5,pady=5)


delete_btn = tk.Button(
    btn_frame,
    text="Delete Task",
    bg="#ff4d4d",
    fg="white",
    width=12,
    command=delete_task
)

delete_btn.grid(row=1,column=0,padx=5,pady=5)


display_btn = tk.Button(
    btn_frame,
    text="Display Tasks",
    bg="#9C27B0",
    fg="white",
    width=12,
    command=display_tasks
)

display_btn.grid(row=1,column=1,padx=5,pady=5)


task_frame = tk.Frame(
    root,
    bg="#f0f8ff",
    bd=2,
    relief="sunken"
)

task_frame.pack(pady=15, padx=20, fill="both", expand=True)

# RUN
root.mainloop()
