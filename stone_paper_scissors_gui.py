import tkinter as tk
from tkinter import messagebox
import random

# Main Window
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("450x400")
root.resizable(False, False)

# Choices
choices = ["Stone", "Paper", "Scissors"]

# Score Variables
user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Display choices
    user_choice_label.config(text=f"You Chose: {user_choice}")
    computer_choice_label.config(
        text=f"Computer Chose: {computer_choice}"
    )

    # Game Logic
    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"

    elif (
        (user_choice == "Stone" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Stone")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        user_score += 1

    else:
        result = "Computer Wins! 💻"
        computer_score += 1

    # Update result and scores
    result_label.config(text=result)
    score_label.config(
        text=f"Your Score: {user_score} | Computer Score: {computer_score}"
    )


def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_choice_label.config(text="You Chose: ")
    computer_choice_label.config(text="Computer Chose: ")
    result_label.config(text="Choose an option to play!")
    score_label.config(text="Your Score: 0 | Computer Score: 0")


# Title
title_label = tk.Label(
    root,
    text="🪨 Stone Paper Scissors ✂️",
    font=("Arial", 18, "bold"),
)
title_label.pack(pady=15)

# Instructions
instruction_label = tk.Label(
    root,
    text="Choose Stone, Paper, or Scissors",
    font=("Arial", 12),
)
instruction_label.pack()

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons
stone_btn = tk.Button(
    button_frame,
    text="🪨 Stone",
    font=("Arial", 12),
    width=12,
    command=lambda: play("Stone"),
)
stone_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 12),
    width=12,
    command=lambda: play("Paper"),
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Arial", 12),
    width=12,
    command=lambda: play("Scissors"),
)
scissors_btn.grid(row=0, column=2, padx=10)

# Labels
user_choice_label = tk.Label(
    root,
    text="You Chose: ",
    font=("Arial", 12),
)
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(
    root,
    text="Computer Chose: ",
    font=("Arial", 12),
)
computer_choice_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="Choose an option to play!",
    font=("Arial", 14, "bold"),
)
result_label.pack(pady=15)

score_label = tk.Label(
    root,
    text="Your Score: 0 | Computer Score: 0",
    font=("Arial", 12),
)
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12),
    bg="lightgray",
    command=reset_game,
)
reset_btn.pack(pady=10)

# Run App
root.mainloop()
