import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QTextEdit, QPushButton, QLineEdit, QHBoxLayout)
from PyQt6.QtCore import Qt

class DiaryApp(QWidget):
    def __init__(self, file_path="diary.txt"):
        super().__init__()
        self.file_path = file_path
        self.all_notes = [] # Cache for searching
        self.init_ui()
        self.load_history()

    def init_ui(self):
        self.setWindowTitle("Professional Diary Dashboard")
        self.resize(450, 600)
        main_layout = QVBoxLayout()

        # Search Bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search history...")
        self.search_input.textChanged.connect(self.filter_history)
        search_layout.addWidget(QLabel("🔍"))
        search_layout.addWidget(self.search_input)
        main_layout.addLayout(search_layout)

        # History Display
        main_layout.addWidget(QLabel("<b>Diary History:</b>"))
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        main_layout.addWidget(self.history_display)

        # New Entry
        main_layout.addWidget(QLabel("<b>New Entry:</b>"))
        self.new_entry_input = QTextEdit()
        self.new_entry_input.setMaximumHeight(80)
        main_layout.addWidget(self.new_entry_input)

        # Save Button
        self.save_button = QPushButton("Save Entry")
        self.save_button.clicked.connect(self.save_entry)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)

    def load_history(self):
        try:
            with open(self.file_path, "r") as file:
                # Splitting by delimiter to handle search easily
                content = file.read()
                self.all_notes = content.split("---------------------------\n")
                self.history_display.setText(content)
        except FileNotFoundError:
            self.history_display.setText("Welcome to your new diary!")

    def save_entry(self):
        text = self.new_entry_input.toPlainText().strip()
        if not text:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d @ %I:%M %p")
        formatted_entry = f"[{timestamp}]\n{text}\n---------------------------\n"
        
        with open(self.file_path, "a") as file:
            file.write(formatted_entry)
        
        self.history_display.append(formatted_entry)
        self.all_notes.append(formatted_entry)
        self.new_entry_input.clear()

    def filter_history(self):
        """Filters the display based on search input."""
        query = self.search_input.text().lower()
        filtered = [note for note in self.all_notes if query in note.lower()]
        self.history_display.setText("---------------------------\n".join(filtered))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiaryApp()
    window.show()
    sys.exit(app.exec())