import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Persistent Diary Dashboard")
window.resize(400, 500)

layout = QVBoxLayout()

# Display area for past notes (Read-Only)
layout.addWidget(QLabel("Diary History:"))
history_display = QTextEdit()
history_display.setReadOnly(True)
history_display.setStyleSheet("background-color: #000000;")
layout.addWidget(history_display)

# Input area for new notes
layout.addWidget(QLabel("New Entry:"))
new_entry_input = QTextEdit()
new_entry_input.setMaximumHeight(100) # Keep input area small
layout.addWidget(new_entry_input)

try:
    with open("diary.txt", "r") as file:
        saved_notes = file.read()
        history_display.setText(saved_notes)
except FileNotFoundError:
    # If this is the very first time running the app, the file won't exist yet.
    history_display.setText("Welcome to your new diary!\n---------------------------\n")

def save_entry():
    # 1. Retrieve and sanitize the text
    entry_text = new_entry_input.toPlainText().strip()
    
    if entry_text == "":
        return # Do nothing if the box is empty
        
    # 2. Generate a formatted timestamp
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d @ %I:%M %p")
    
    # 3. Format the final string
    formatted_entry = f"[{timestamp}]\n{entry_text}\n---------------------------\n"
    
    # 4. Save permanently to the hard drive
    with open("diary.txt", "a") as file:
        file.write(formatted_entry)
        
    # 5. Update the UI and clear the input box
    history_display.append(formatted_entry)
    new_entry_input.clear()

save_button = QPushButton("Save Entry")
save_button.clicked.connect(save_entry)
layout.addWidget(save_button)
window.setLayout(layout)
window.show()
sys.exit(app.exec())