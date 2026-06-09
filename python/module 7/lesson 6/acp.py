# Import necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox
import random

# Define the Rock Paper Scissors App class
class RockPaperScissorsApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x400")

        # Choices
        self.choices = ["Rock", "Paper", "Scissors"]

        # Heading
        ttk.Label(
            root,
            text="Rock Paper Scissors Game",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        # Player Choice Label
        ttk.Label(
            root,
            text="Choose your move:",
            font=("Arial", 12)
        ).pack(pady=10)

        # Dropdown Menu
        self.choice_var = tk.StringVar()
        self.choice_box = ttk.Combobox(
            root,
            textvariable=self.choice_var,
            values=self.choices,
            state="readonly",
            width=20
        )

        self.choice_box.pack(pady=10)
        self.choice_box.current(0)

        # Play Button
        play_button = ttk.Button(
            root,
            text="Play",
            command=self.play_game
        )
        play_button.pack(pady=10)

        # Result Labels
        self.user_label = ttk.Label(root, text="")
        self.user_label.pack(pady=5)

        self.computer_label = ttk.Label(root, text="")
        self.computer_label.pack(pady=5)

        self.result_label = ttk.Label(
            root,
            text="",
            font=("Arial", 14, "bold")
        )
        self.result_label.pack(pady=20)

    # Method to play the game
    def play_game(self):

        user_choice = self.choice_var.get()
        computer_choice = random.choice(self.choices)

        self.user_label.config(
            text=f"Your Choice: {user_choice}"
        )

        self.computer_label.config(
            text=f"Computer Choice: {computer_choice}"
        )

        # Decide winner
        if user_choice == computer_choice:
            result = "It's a Tie!"

        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win!"

        else:
            result = "Computer Wins!"

        self.result_label.config(text=result)


# Main block
if __name__ == "__main__":

    root = tk.Tk()

    app = RockPaperScissorsApp(root)

    root.mainloop()