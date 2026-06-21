import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Test Grade Evaluator")
window.resize(300, 200)

layout = QVBoxLayout()

# UI Elements
layout.addWidget(QLabel("Enter numeric score (0-100):"))
score_entry = QLineEdit()
layout.addWidget(score_entry)

result_label = QLabel("Grade: --")
# Make the font larger and bold
result_label.setStyleSheet("font-size: 16px; font-weight: bold;")
layout.addWidget(result_label)

def evaluate_score():
    try:
        score = float(score_entry.text())
        
        if score >= 90:
            result_label.setText("Grade: A (Pass)")
            result_label.setStyleSheet("color: green; font-size: 16px; font-weight: bold;")
        elif score >= 80:
            result_label.setText("Grade: B (Pass)")
            result_label.setStyleSheet("color: green; font-size: 16px; font-weight: bold;")
        elif score >= 70:
            result_label.setText("Grade: C (Pass)")
            result_label.setStyleSheet("color: orange; font-size: 16px; font-weight: bold;")
        elif score >= 60:
            result_label.setText("Grade: D (Pass)")
            result_label.setStyleSheet("color: orange; font-size: 16px; font-weight: bold;")
        elif score >= 50:
            result_label.setText("Grade: E (Fail)")
            result_label.setStyleSheet("color: red; font-size: 16px; font-weight: bold;")
        else:
            result_label.setText("Grade: F (Fail)")
            result_label.setStyleSheet("color: red; font-size: 16px; font-weight: bold;")
            
    except ValueError:
        result_label.setText("Error: Enter a valid number.")
        result_label.setStyleSheet("color: red; font-size: 16px; font-weight: bold;")
eval_btn = QPushButton("Evaluate")
eval_btn.clicked.connect(evaluate_score)
layout.addWidget(eval_btn)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
