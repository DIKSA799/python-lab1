import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QLineEdit,
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Persistent Diary Dashboard")
window.resize(400, 550)

layout = QVBoxLayout()

# Search section
layout.addWidget(QLabel("Search Entry or Date:"))
search_input = QLineEdit()
search_input.setPlaceholderText("Enter text or date (YYYY-MM-DD)")
layout.addWidget(search_input)

search_button = QPushButton("Search")
layout.addWidget(search_button)

# History display
layout.addWidget(QLabel("Diary History:"))
history_display = QTextEdit()
history_display.setReadOnly(True)
history_display.setStyleSheet("background-color: #000000; color: white;")
layout.addWidget(history_display)

# New entry section
layout.addWidget(QLabel("New Entry:"))
new_entry_input = QTextEdit()
new_entry_input.setMaximumHeight(100)
layout.addWidget(new_entry_input)


def load_entries():
    try:
        with open("diary.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Welcome to your new diary!\n---------------------------\n"


history_display.setText(load_entries())


def search_entries():
    keyword = search_input.text().strip().lower()

    if not keyword:
        history_display.setText(load_entries())
        return

    try:
        with open("diary.txt", "r") as file:
            content = file.read()

        entries = content.split("---------------------------")
        results = []

        for entry in entries:
            if keyword in entry.lower():
                results.append(entry.strip())

        if results:
            history_display.setText(
                "\n---------------------------\n".join(results)
            )
        else:
            history_display.setText("No matching entries found.")

    except FileNotFoundError:
        history_display.setText("No diary entries found.")


def save_entry():
    entry_text = new_entry_input.toPlainText().strip()

    if not entry_text:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d @ %I:%M %p")

    formatted_entry = (
        f"[{timestamp}]\n"
        f"{entry_text}\n"
        "---------------------------\n"
    )

    with open("diary.txt", "a") as file:
        file.write(formatted_entry)

    history_display.append(formatted_entry)
    new_entry_input.clear()


save_button = QPushButton("Save Entry")
save_button.clicked.connect(save_entry)

search_button.clicked.connect(search_entries)

layout.addWidget(save_button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())