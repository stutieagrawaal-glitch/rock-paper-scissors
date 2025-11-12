#rock paper scissors game
import tkinter as tk

import random
while True:
    options = ['rock','scissors','paper']
    object = random.choice(options)
    player_score = 0
    computer_score = 0
    counter = input("choose from rock,paper or scissors: ").lower()
    if object == "rock" and counter == "paper" :
        print("you won!!")
        print("i chose: ", object)
        player_score += 1
        print(player_score)
    elif object == "rock" and counter == "rock":
        print("its a tie!")
        print("i chose: ", object)
    elif object == "scissors" and counter == "rock":
        print("you won!!")
        print("i chose: ", object)
        player_score += 1
        print(player_score)
    elif object == "scissors" and counter == "scissors":
        print("its a tie!")
        print("i chose: ", object)
    elif object == "paper" and counter == "rock":
        print("you won!!")
        print("i chose: ", object)
        player_score += 1
        print(player_score)
    elif object == "paper" and counter == "paper":
        print("its a tie!")
        print("i chose: ", object)
    else:
        print("you lost!")
        print("i chose: ", object)
        computer_score += 1
        print(computer_score)
    # --- 3. Update GUI elements ---
    
    # Update the label showing what both players chose
    choice_label.config(text=f"Your choice: {user_choice.capitalize()} | Computer choice: {computer_choice.capitalize()}")
    
    # Update the result label
    result_label.config(text=result_text, font=('Arial', 14, 'bold'))
    
    # Update the score display
    score_label.config(text=f"Score: Player {player_score} - Computer {computer_score}")
    # Initialize the main window
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    root.geometry("400x350") # Set a fixed size
#   Configure font for better readability
    FONT_STYLE = ('Arial', 12)
# --- 1. Title and Choice Buttons ---

    title_label = tk.Label(root, text="Make Your Move!", font=('Arial', 16, 'underline'))
    title_label.pack(pady=10)

# Create a Frame to hold the buttons horizontally
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

# Create the three buttons. The 'lambda' function is crucial 
# because it lets you pass an argument to play_game() when the button is clicked.

    rock_button = tk.Button(button_frame, text="✊ ROCK", command=lambda: play_game("rock"), width=12, height=2, font=FONT_STYLE)
    paper_button = tk.Button(button_frame, text="✋ PAPER", command=lambda: play_game("paper"), width=12, height=2, font=FONT_STYLE)
    scissors_button = tk.Button(button_frame, text="✌️ SCISSORS", command=lambda: play_game("scissors"), width=12, height=2, font=FONT_STYLE)

# Use pack with 'side=tk.LEFT' to arrange them in a row
    rock_button.pack(side=tk.LEFT, padx=5)
    paper_button.pack(side=tk.LEFT, padx=5)
    scissors_button.pack(side=tk.LEFT, padx=5)


# --- 2. Output Labels ---

# Label to show the choices made
    choice_label = tk.Label(root, text="Choices will appear here...", font=('Arial', 10), pady=5)
    choice_label.pack()

# Label to show the result (Win/Loss/Tie)
    result_label = tk.Label(root, text="Press a button to start the game!", font=('Arial', 14))
    result_label.pack(pady=10)

# --- 3. Score Tracker ---

    score_label = tk.Label(root, text=f"Score: Player {player_score} - Computer {computer_score}", font=('Arial', 12, 'italic'), fg='blue')
    score_label.pack(pady=10)


# Start the main event loop - this makes the window appear and waits for interaction
    root.mainloop()