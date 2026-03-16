import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# MAIN WINDOW 

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("550x620")
root.configure(bg="#2C2F4F")

# START SCREEN 

start_frame = tk.Frame(root, bg="#2C2F4F")
start_frame.pack(fill="both", expand=True)

title = tk.Label(start_frame,
                 text="🎮 Rock Paper Scissors",
                 font=("Comic Sans MS", 26, "bold"),
                 bg="#2C2F4F",
                 fg="white")
title.pack(pady=80)

instruction_start = tk.Label(start_frame,
                             text="Press Start to begin the game",
                             font=("Comic Sans MS", 14),
                             bg="#2C2F4F",
                             fg="lightgray")
instruction_start.pack(pady=10)

countdown_label = tk.Label(start_frame,
                           text="",
                           font=("Comic Sans MS", 50, "bold"),
                           bg="#2C2F4F",
                           fg="cyan")
countdown_label.pack(pady=20)

# GAME SCREEN

game_frame = tk.Frame(root, bg="#2C2F4F")

def show_game():
    start_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

# COUNTDOWN

def start_game():
    countdown_label.config(text="3")
    root.after(800, lambda: countdown_label.config(text="2"))
    root.after(1600, lambda: countdown_label.config(text="1"))
    root.after(2400, lambda: countdown_label.config(text="🎮 GO!"))
    root.after(3200, show_game)

start_button = tk.Button(start_frame,
                         text="Start Game",
                         font=("Comic Sans MS", 16, "bold"),
                         bg="#FF6B6B",
                         fg="white",
                         width=15,
                         command=start_game)
start_button.pack(pady=20)

# GAME LOGIC 

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "😐 It's a Tie!"
        result_label.config(fg="yellow")

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        result = "🎉 You Win!"
        result_label.config(fg="lightgreen")
        user_score += 1

    else:
        result = "💻 Computer Wins!"
        result_label.config(fg="orange")
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Score  You: {user_score} | Computer: {computer_score}"
    )

    feedback_label.config(
        text="Click 'Play Again' to start another round!"
    )

    play_again_btn.pack(pady=10)


# PLAY AGAIN FUNCTION

def play_again():
    user_label.config(text="Your Choice:")
    computer_label.config(text="Computer Choice:")
    result_label.config(text="Result will appear here", fg="white")
    feedback_label.config(text="Choose Rock, Paper, or Scissors to play")
    play_again_btn.pack_forget()

# GAME UI

title2 = tk.Label(game_frame,
                  text="Make Your Move!",
                  font=("Comic Sans MS", 20, "bold"),
                  bg="#2C2F4F",
                  fg="white")
title2.pack(pady=20)

instruction_game = tk.Label(game_frame,
                            text="Choose Rock, Paper, or Scissors",
                            font=("Comic Sans MS", 13),
                            bg="#2C2F4F",
                            fg="lightgray")
instruction_game.pack()

button_frame = tk.Frame(game_frame, bg="#2C2F4F")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame,
                     text="🪨 Rock",
                     font=("Comic Sans MS", 14, "bold"),
                     width=12,
                     height=2,
                     bg="#6BCB77",
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(button_frame,
                      text="📄 Paper",
                      font=("Comic Sans MS", 14, "bold"),
                      width=12,
                      height=2,
                      bg="#4D96FF",
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = tk.Button(button_frame,
                         text="✂️ Scissors",
                         font=("Comic Sans MS", 14, "bold"),
                         width=12,
                         height=2,
                         bg="#FFD93D",
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=15)

# RESULT AREA

user_label = tk.Label(game_frame,
                      text="Your Choice:",
                      font=("Comic Sans MS", 13),
                      bg="#2C2F4F",
                      fg="white")
user_label.pack(pady=5)

computer_label = tk.Label(game_frame,
                          text="Computer Choice:",
                          font=("Comic Sans MS", 13),
                          bg="#2C2F4F",
                          fg="white")
computer_label.pack(pady=5)

result_label = tk.Label(game_frame,
                        text="Result will appear here",
                        font=("Comic Sans MS", 18, "bold"),
                        bg="#2C2F4F",
                        fg="white")
result_label.pack(pady=20)

score_label = tk.Label(game_frame,
                       text="Score  You: 0 | Computer: 0",
                       font=("Comic Sans MS", 15),
                       bg="#2C2F4F",
                       fg="white")
score_label.pack(pady=10)

feedback_label = tk.Label(game_frame,
                          text="Choose Rock, Paper, or Scissors to play",
                          font=("Comic Sans MS", 12),
                          bg="#2C2F4F",
                          fg="lightgray")
feedback_label.pack(pady=10)

play_again_btn = tk.Button(game_frame,
                           text="🔁 Play Again",
                           font=("Comic Sans MS", 13, "bold"),
                           bg="#FF6B6B",
                           fg="white",
                           width=15,
                           command=play_again)

root.mainloop()