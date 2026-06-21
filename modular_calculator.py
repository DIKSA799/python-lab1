import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

#bussiness Logic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error" # Prevent division by zero
    return a / b

#front end
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Modular Calculator")

main_layout = QVBoxLayout()
display = QLineEdit()
display.setReadOnly(True) # Prevent user from typing letters directly
display.setStyleSheet("font-size: 20px; padding: 5px;")
main_layout.addWidget(display)

grid = QGridLayout()
main_layout.addLayout(grid)

first_number = 0.0
current_operator = ""
is_new_input = True

def button_click(value):
    global is_new_input
    if is_new_input:
        display.setText(value)
        is_new_input = False
    else:
        display.setText(display.text() + value)

def set_operator(op):
    global first_number, current_operator, is_new_input
    first_number = float(display.text())
    current_operator = op
    is_new_input = True

def calculate_result():
    global is_new_input
    second_number = float(display.text())
    result = 0
    
    # Call our isolated business logic functions
    if current_operator == "+":
        result = add(first_number, second_number)
    elif current_operator == "-":
        result = subtract(first_number, second_number)
    elif current_operator == "*":
        result = multiply(first_number, second_number)
    elif current_operator == "/":
        result = divide(first_number, second_number)
        
    display.setText(str(result))
    is_new_input = True

def clear_display():
    global first_number, current_operator, is_new_input
    first_number = 0.0
    current_operator = ""
    is_new_input = True
    display.clear()
# Row 0
btn_7 = QPushButton("7"); btn_7.clicked.connect(lambda: button_click("7"))
btn_8 = QPushButton("8"); btn_8.clicked.connect(lambda: button_click("8"))
btn_9 = QPushButton("9"); btn_9.clicked.connect(lambda: button_click("9"))
btn_div = QPushButton("/"); btn_div.clicked.connect(lambda: set_operator("/"))
grid.addWidget(btn_7, 0, 0); grid.addWidget(btn_8, 0, 1); grid.addWidget(btn_9, 0, 2); grid.addWidget(btn_div, 0, 3)

# Row 1
btn_4 = QPushButton("4"); btn_4.clicked.connect(lambda: button_click("4"))
btn_5 = QPushButton("5"); btn_5.clicked.connect(lambda: button_click("5"))
btn_6 = QPushButton("6"); btn_6.clicked.connect(lambda: button_click("6"))
btn_mult = QPushButton("*"); btn_mult.clicked.connect(lambda: set_operator("*"))
grid.addWidget(btn_4, 1, 0); grid.addWidget(btn_5, 1, 1); grid.addWidget(btn_6, 1, 2); grid.addWidget(btn_mult, 1, 3)

# Row 2
btn_1 = QPushButton("1"); btn_1.clicked.connect(lambda: button_click("1"))
btn_2 = QPushButton("2"); btn_2.clicked.connect(lambda: button_click("2"))
btn_3 = QPushButton("3"); btn_3.clicked.connect(lambda: button_click("3"))
btn_minus = QPushButton("-"); btn_minus.clicked.connect(lambda: set_operator("-"))
grid.addWidget(btn_1, 2, 0); grid.addWidget(btn_2, 2, 1); grid.addWidget(btn_3, 2, 2); grid.addWidget(btn_minus, 2, 3)

# Row 3
btn_clear = QPushButton("C"); btn_clear.clicked.connect(clear_display)
btn_0 = QPushButton("0"); btn_0.clicked.connect(lambda: button_click("0"))
btn_equals = QPushButton("="); btn_equals.clicked.connect(calculate_result)
btn_plus = QPushButton("+"); btn_plus.clicked.connect(lambda: set_operator("+"))
grid.addWidget(btn_clear, 3, 0); grid.addWidget(btn_0, 3, 1); grid.addWidget(btn_equals, 3, 2); grid.addWidget(btn_plus, 3, 3)

window.setLayout(main_layout)
window.show()
sys.exit(app.exec())
