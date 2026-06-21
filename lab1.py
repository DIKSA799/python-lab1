# Hello world with pyqt6
import sys
import PyQt6.QtWidgets as QtWidgets
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
# Set the window title
window.setWindowTitle('Hello World with PyQt6')
#Add label to the window
widget = QtWidgets.QLabel('Hello, World!', parent=window)
widget.move(150, 130)
# Set the window size
window.resize(400, 300)
# Show the window
window.show()
# Start the event loop
sys.exit(app.exec())    