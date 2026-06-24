import sys;from PyQt6.QtWidgets import *
app=QApplication(sys.argv)
w=QWidget()
l=QVBoxLayout()
x=QLineEdit()
l.addWidget(x)
lbl=QLabel("result")
l.addWidget(lbl)
def DO_STUFF():
    try:
        a=float(x.text())
        ans=a*2.20462
        lbl.setText(str(ans))
    except:
        lbl.setText("err")
b=QPushButton("go")
b.clicked.connect(DO_STUFF)
l.addWidget(b)
w.setLayout(l);w.show();sys.exit(app.exec())
