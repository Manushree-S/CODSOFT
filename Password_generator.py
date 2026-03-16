import tkinter as tk
from tkinter import ttk
import random
import string

history = []

# PASSWORD GENERATION

def generate_password():

    try:
        length = int(length_entry.get())
    except:
        password_var.set("Enter a valid number!")
        return

    if length < 4:
        password_var.set("Length must be ≥ 4")
        return

    char_sets = []

    if lower_var.get():
        char_sets.append(string.ascii_lowercase)

    if upper_var.get():
        char_sets.append(string.ascii_uppercase)

    if number_var.get():
        char_sets.append(string.digits)

    if symbol_var.get():
        char_sets.append(string.punctuation)

    if not char_sets:
        password_var.set("Select at least one option!")
        return

    progress.start(10)

    animate_text(length, char_sets, 0)


def animate_text(length, char_sets, count):

    all_chars = "".join(char_sets)

    if count < 15:
        fake = "".join(random.choice(all_chars) for _ in range(length))
        password_var.set(fake)

        root.after(80, animate_text, length, char_sets, count + 1)

    else:

        password_chars = [random.choice(char_set) for char_set in char_sets]

        while len(password_chars) < length:
            password_chars.append(random.choice(all_chars))

        random.shuffle(password_chars)

        final_password = "".join(password_chars)

        password_var.set(final_password)

        progress.stop()

        add_to_history(final_password)
        check_strength(final_password)


# PASSWORD STRENGTH

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 1:
        strength_label.config(text="Strength: Weak", fg="red")

    elif score == 2:
        strength_label.config(text="Strength: Medium", fg="orange")

    else:
        strength_label.config(text="Strength: Strong", fg="lightgreen")


# PASSWORD HISTORY 

def add_to_history(password):

    history.append(password)

    history_box.delete(0, tk.END)

    for p in history[-10:]:
        history_box.insert(tk.END, p)


# COPY PASSWORD 

def copy_password():

    root.clipboard_clear()
    root.clipboard_append(password_var.get())


# WINDOW

root = tk.Tk()
root.title("Smart Password Generator")
root.geometry("620x620")
root.configure(bg="#0F172A")


title = tk.Label(root,
                 text="🔐 Smart Password Generator",
                 font=("Courier",22,"bold"),
                 fg="#22C55E",
                 bg="#0F172A")

title.pack(pady=15)


instruction = tk.Label(root,
                       text="Enter password length and select options",
                       font=("Arial",11),
                       fg="lightgray",
                       bg="#0F172A")

instruction.pack()


# PASSWORD DISPLAY

password_var = tk.StringVar()

password_entry = tk.Entry(root,
                          textvariable=password_var,
                          font=("Courier",18),
                          justify="center",
                          width=28,
                          bg="#020617",
                          fg="#22C55E")

password_entry.pack(pady=20)


# LENGTH INPUT

length_label = tk.Label(root,
                        text="Enter Password Length",
                        bg="#0F172A",
                        fg="white")

length_label.pack()

length_entry = tk.Entry(root,
                        font=("Arial",12),
                        width=10,
                        justify="center")

length_entry.pack(pady=10)


# OPTIONS

lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar()
number_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

options_frame = tk.Frame(root, bg="#0F172A")
options_frame.pack(pady=5)

tk.Checkbutton(options_frame, text="Lowercase",
               variable=lower_var,
               bg="#0F172A", fg="white",
               selectcolor="#0F172A").grid(row=0,column=0,padx=10)

tk.Checkbutton(options_frame, text="Uppercase",
               variable=upper_var,
               bg="#0F172A", fg="white",
               selectcolor="#0F172A").grid(row=0,column=1,padx=10)

tk.Checkbutton(options_frame, text="Numbers",
               variable=number_var,
               bg="#0F172A", fg="white",
               selectcolor="#0F172A").grid(row=0,column=2,padx=10)

tk.Checkbutton(options_frame, text="Symbols",
               variable=symbol_var,
               bg="#0F172A", fg="white",
               selectcolor="#0F172A").grid(row=0,column=3,padx=10)



# GENERATE BUTTON 

generate_btn = tk.Button(root,
                         text="Generate Password",
                         font=("Arial",13,"bold"),
                         bg="#22C55E",
                         fg="black",
                         width=20,
                         command=generate_password)

generate_btn.pack(pady=20)


# PROGRESS BAR 

progress = ttk.Progressbar(root,
                           orient="horizontal",
                           length=300,
                           mode="indeterminate")

progress.pack(pady=10)


# STRENGTH

strength_label = tk.Label(root,
                          text="Strength:",
                          font=("Arial",13,"bold"),
                          bg="#0F172A",
                          fg="white")

strength_label.pack(pady=5)


# COPY BUTTON

copy_btn = tk.Button(root,
                     text="Copy Password",
                     bg="#3B82F6",
                     fg="white",
                     command=copy_password)

copy_btn.pack(pady=10)


# HISTORY

history_label = tk.Label(root,
                         text="Password History",
                         font=("Arial",12,"bold"),
                         bg="#0F172A",
                         fg="white")

history_label.pack(pady=5)

history_box = tk.Listbox(root,
                         width=45,
                         height=8)

history_box.pack(pady=10)


root.mainloop()