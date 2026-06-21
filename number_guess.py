import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# State Variables
secret_number = random.randint(1, 100)
attempts_remaining = 20

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Guess the Number")

layout = QVBoxLayout()

instruction = QLabel("Guess a number between 1 and 100:")
layout.addWidget(instruction)

guess_entry = QLineEdit()
layout.addWidget(guess_entry)

feedback_label = QLabel(f"Attempts remaining: {attempts_remaining}")
layout.addWidget(feedback_label)
#Game logic
def check_guess():
    global attempts_remaining 
    
    guess = int(guess_entry.text())
    attempts_remaining -= 1
    
    if guess == secret_number:
        feedback_label.setText("Correct! You win!")
        feedback_label.setStyleSheet("color: green; font-weight: bold;")
        guess_btn.setEnabled(False) # Disable button on win
    elif attempts_remaining == 0:
        feedback_label.setText(f"Game Over. The number was {secret_number}.")
        feedback_label.setStyleSheet("color: red; font-weight: bold;")
        guess_btn.setEnabled(False) # Disable button on loss
    elif guess > secret_number:
        feedback_label.setText(f"Too High! Attempts remaining: {attempts_remaining}")
    elif guess < secret_number:
        feedback_label.setText(f"Too Low! Attempts remaining: {attempts_remaining}")
        
    guess_entry.clear() # Clear the input box for the next loop

guess_btn = QPushButton("Submit Guess")
guess_btn.clicked.connect(check_guess)
layout.addWidget(guess_btn)

window.setLayout(layout)
window.show()
sys.exit(app.exec())


