from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from os import system

system("cls || clear")

class Button(QPushButton):
    def __init__(self, window: QWidget, x: int, y: int, w: int, h: int, s: str):
        super().__init__(window)
        self.setGeometry(x, y, w, h)
        self.setText(s)
        self.setStyleSheet("""
            border-radius: 15px;
            font-size: 25px;
            background-color: #d5d8dc;
        """)

class Button2(QPushButton):
    def __init__(self, window: QWidget, x: int, y: int, w: int, h: int, s: str):
        super().__init__(window)
        self.setGeometry(x, y, w, h)
        self.setText(s)
        self.setStyleSheet("""
            border-radius: 15px;
            font-size: 25px;
            background-color: #abb2b9;
        """)


app = QApplication([])

oyna = QWidget()
oyna.setFixedSize(405, 500)
oyna.setWindowTitle("Kalkulyator")

edit = QLineEdit(oyna)
edit.setGeometry(7, 10, 391, 80)
edit.setStyleSheet("""
    border-radius: 8px;
    background-color: #abb2b9;
    font-size: 32px;
""")
edit.setAlignment(Qt.AlignRight)
edit.setText("0")

b0 = Button(oyna, 7, 420, 193, 70, "0")
bnuqta = Button(oyna, 205, 420, 94, 70, ".")
b1 = Button(oyna, 7, 345, 94, 70, "1")
b2 = Button(oyna, 106, 345, 94, 70, "2")
b3 = Button(oyna, 205, 345, 94, 70, "3")
b4 = Button(oyna, 7, 270, 94, 70, "4")
b5 = Button(oyna, 106, 270, 94, 70, "5")
b6 = Button(oyna, 205, 270, 94, 70, "6")
b7 = Button(oyna, 7, 195, 94, 70, "7")
b8 = Button(oyna, 106, 195, 94, 70, "8")
b9 = Button(oyna, 205, 195, 94, 70, "9")

bplus = Button2(oyna, 304, 345, 94, 70, "+")
bminus = Button2(oyna, 304, 270, 94, 70, "-")
bkarra = Button2(oyna, 304, 195, 94, 70, "×")
bbolish = Button2(oyna, 304, 120, 94, 70, "÷")
bteng = Button(oyna, 304, 420, 94, 70, "=")
bteng.setStyleSheet("""
    font-size: 25px;
    border-radius: 15px;
    background-color: #808b96;
""")

bc = Button2(oyna, 7, 120, 193, 70, "C")
b = Button2(oyna, 205, 120, 94, 70, "⌫")

# Asosiy o'zgaruvchilar
mains = "0"


def oxirgison(s: str) ->str:
    n = ""
    for i in s[::-1]:
        if not i in ["+", "-", "*", "/"]:
            n += i
        else:
            break
    return n[::-1]

def raqam(n: str):
    global mains
    son = oxirgison(mains)
    if n == "." and not son == "" and not n in son:
        mains += n
    elif n == "." and son == "":
        mains += "0."
    elif (n == "0" and not son == "" and (not son[0] == "0" or "." in son)) or (n == "0" and son == ""):
        mains += "0"
    elif n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9":
        if len(son) == 1 and son[0] == "0":
            mains = mains[:len(mains) - 1]
            mains += n
        else:
            mains += n
    edit.setText(mains)

def amaluchun(n: str):
    global mains
    if mains[-1] == ".":
        mains += "0" + n
    elif not mains[-1] in ["+", "-", "*", "/"]:
        mains += n
    else:
        mains = mains[:len(mains) - 1]
        mains += n
    edit.setText(mains)

def tenglik():
    global mains
    try:
        mains = str(eval(mains))
        edit.setText(mains)
    except:
        edit.setText("Xatolik")
        mains = ""

def clearfunc():
    global mains
    mains = "0"
    edit.setText(mains)

def popfunc():
    global mains
    if len(mains) == 1:
        mains = "0"
    else:
        mains = mains[:len(mains) - 1]
    edit.setText(mains)

b0.clicked.connect(lambda: raqam("0"))
b1.clicked.connect(lambda: raqam("1"))
b2.clicked.connect(lambda: raqam("2"))
b3.clicked.connect(lambda: raqam("3"))
b4.clicked.connect(lambda: raqam("4"))
b5.clicked.connect(lambda: raqam("5"))
b6.clicked.connect(lambda: raqam("6"))
b7.clicked.connect(lambda: raqam("7"))
b8.clicked.connect(lambda: raqam("8"))
b9.clicked.connect(lambda: raqam("9"))
bnuqta.clicked.connect(lambda: raqam("."))

bplus.clicked.connect(lambda: amaluchun("+"))
bminus.clicked.connect(lambda: amaluchun("-"))
bkarra.clicked.connect(lambda: amaluchun("*"))
bbolish.clicked.connect(lambda: amaluchun("/"))

bteng.clicked.connect(tenglik)

bc.clicked.connect(clearfunc)
b.clicked.connect(popfunc)

oyna.show()
app.exec()