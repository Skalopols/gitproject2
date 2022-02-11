import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from UI import Ui_MainWindow

Collor = [QColor(255, 255, 0), QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255)]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.radius = random.randint(50, 150)
        self.radius2 = random.randint(50, 150)
        self.radius3 = random.randint(50, 150)
        self.x1, self.y1 = random.randint(50, 800), random.randint(50, 800)
        self.x2, self.y2 = random.randint(50, 950), random.randint(50, 800)
        self.x3, self.y3 = random.randint(50, 650), random.randint(50, 800)
        self.c1 = random.randint(0, 3)
        self.c2 = random.randint(0, 3)
        self.c3 = random.randint(0, 3)
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(Collor[self.c1])
        qp.drawEllipse(self.x1, self.y1, self.radius, self.radius)
        qp.setBrush(Collor[self.c2])
        qp.drawEllipse(self.x2, self.y2, self.radius2, self.radius2)
        qp.setBrush(Collor[self.c3])
        qp.drawEllipse(self.x3, self.y3, self.radius3, self.radius3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
