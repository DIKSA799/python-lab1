import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

# Global Dictionary
students = {}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Student Record System")
window.resize(350, 450)

layout = QVBoxLayout()

# Form Widgets
layout.addWidget(QLabel("Student ID:"))
id_entry = QLineEdit()
layout.addWidget(id_entry)

layout.addWidget(QLabel("Student Name:"))
name_entry = QLineEdit()
layout.addWidget(name_entry)

layout.addWidget(QLabel("Grade (e.g., A, B, C):"))
grade_entry = QLineEdit()
layout.addWidget(grade_entry)

layout.addWidget(QLabel("Gender (M/F):"))
gender_entry = QLineEdit()
layout.addWidget(gender_entry)

add_btn = QPushButton("Add/Update Student")
layout.addWidget(add_btn)

# Search Widgets
layout.addWidget(QLabel("--- Search ---"))
search_entry = QLineEdit()
search_entry.setPlaceholderText("Enter Student ID to Search")
layout.addWidget(search_entry)

search_btn = QPushButton("Find Student")
layout.addWidget(search_btn)

# List Display Widget
layout.addWidget(QLabel("--- All Records ---"))
record_list = QListWidget()
layout.addWidget(record_list)

def update_display():
    # 1. Clear the old list
    record_list.clear()
    
    # 2. Iterate through the dictionary and add items
    for student_id, details in students.items():
        # Using a tuple/f-string to format the display cleanly
        display_text = f"ID: {student_id} | {details['name']} | {details['gender']}| Grade: {details['grade']}"
        record_list.addItem(display_text)

def add_student():
    s_id = id_entry.text()
    s_name = name_entry.text()
    s_gender = gender_entry.text()
    s_grade = grade_entry.text()

    
    if s_id == "" or s_name == "":
        return # Basic validation to prevent empty data
        
    # Add to dictionary (Key: ID, Value: Dictionary of details)
    students[s_id] = {"name": s_name, "gender": s_gender, "grade": s_grade}
    
    # Clear the form
    id_entry.clear(); name_entry.clear(); grade_entry.clear(); gender_entry.clear()
    
    # Refresh the UI list
    update_display()

def search_student():
    search_id = search_entry.text()
    
    # Dictionary lookup
    if search_id in students:
        student = students[search_id]
        QMessageBox.information(window, "Student Found", 
            f"Name: {student['name']}\nGender: {student['gender']}\nGrade: {student['grade']}")
    else:
        QMessageBox.warning(window, "Not Found", "Student ID does not exist.")
        
    search_entry.clear()
add_btn.clicked.connect(add_student)
search_btn.clicked.connect(search_student)

window.setLayout(layout)
window.show()
sys.exit(app.exec())




