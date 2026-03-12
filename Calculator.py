import tkinter as tk

# DATA 

history = []

# FUNCTIONS

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def percentage():
    display.insert(tk.END, "%")

def calculate():
    try:
        expression = display.get()

        # case 1: number%
        if expression.endswith("%") and expression.count("%") == 1:
            number = float(expression[:-1])
            result = number / 100

        # case 2: invalid percentage usage
        elif "%" in expression:
            raise Exception("Invalid percentage")

        # normal calculation
        else:
            result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

        history.append(f"{expression} = {result}")
        update_history()

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def update_history():
    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)

# WINDOW

root = tk.Tk()
root.title("My Calculator")
root.geometry("420x550")
root.configure(bg="#0f0f0f")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=5)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)

# DISPLAY

display = tk.Entry(
    root,
    font=("Segoe UI", 28),
    bg="#0f0f0f",
    fg="white",
    bd=0,
    insertbackground="white",
    justify="right"
)

display.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=15, pady=20)

# BUTTON FRAME

frame = tk.Frame(root, bg="#0f0f0f")
frame.grid(row=1, column=0, sticky="nsew")

for i in range(5):
    frame.rowconfigure(i, weight=1)

for j in range(4):
    frame.columnconfigure(j, weight=1)

# COLORS

num_color = "#2b2b2b"
operator_color = "#ff9500"
text_color = "white"

# BUTTONS

buttons = [

    ("AC", clear, operator_color),
    ("⌫", backspace, operator_color),
    ("%", percentage, operator_color),
    ("/", lambda: press("/"), operator_color),

    ("7", lambda: press("7"), num_color),
    ("8", lambda: press("8"), num_color),
    ("9", lambda: press("9"), num_color),
    ("*", lambda: press("*"), operator_color),

    ("4", lambda: press("4"), num_color),
    ("5", lambda: press("5"), num_color),
    ("6", lambda: press("6"), num_color),
    ("-", lambda: press("-"), operator_color),

    ("1", lambda: press("1"), num_color),
    ("2", lambda: press("2"), num_color),
    ("3", lambda: press("3"), num_color),
    ("+", lambda: press("+"), operator_color),

    ("0", lambda: press("0"), num_color),
    (".", lambda: press("."), num_color),
    ("=", calculate, operator_color),
]

row = 0
col = 0

for (text, command, color) in buttons:

    btn = tk.Button(
        frame,
        text=text,
        command=command,
        bg=color,
        fg=text_color,
        font=("Segoe UI", 16),
        bd=0,
        activebackground="#444"
    )

    btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)

    col += 1

    if col > 3:
        col = 0
        row += 1

# HISTORY PANEL

history_frame = tk.Frame(root, bg="#1a1a1a")
history_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

tk.Label(
    history_frame,
    text="History",
    bg="#1a1a1a",
    fg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

history_box = tk.Listbox(
    history_frame,
    bg="#1a1a1a",
    fg="white",
    bd=0
)

history_box.pack(fill="both", expand=True, padx=5, pady=5)

# RUN

root.mainloop()