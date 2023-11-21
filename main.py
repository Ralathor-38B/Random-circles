import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Random circles')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(200, 35)
        self.do_paint = False
        self.btn.clicked.connect(self.circle)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            radius = randint(25, 150)
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            qp.begin(self)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(250 - radius, 250 - radius, 2 * radius, 2 * radius)
            qp.end()
        self.do_paint = False

    def circle(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
