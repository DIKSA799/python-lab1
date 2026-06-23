# clean_code.py

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def convert_weight():
    """Convert kilograms to pounds."""
    try:
        kilograms = float(weight_input.text())
        pounds = kilograms * 2.20462
        result_label.setText(f"{pounds:.2f}")
    except ValueError:
        result_label.setText("Error")


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Weight Converter")

layout = QVBoxLayout()

weight_input = QLineEdit()
layout.addWidget(weight_input)

result_label = QLabel("Result")
layout.addWidget(result_label)

convert_button = QPushButton("Go")
convert_button.clicked.connect(convert_weight)
layout.addWidget(convert_button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())