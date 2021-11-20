import sys

from random import randrange
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Button')

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("ufo.png"))
        self.label.move(0, 0)
        self.label.resize(32, 32)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.label.move(self.label.x() + 5, self.label.y())
        elif event.key() == Qt.Key_Left:
            self.label.move(self.label.x() - 5, self.label.y())
        elif event.key() == Qt.Key_Up:
            self.label.move(self.label.x(), self.label.y() - 5)
        elif event.key() == Qt.Key_Down:
            self.label.move(self.label.x(), self.label.y() + 5)
        self.check_coord()

    def check_coord(self):
        x = self.label.x()
        y = self.label.y()

        if x > 400:
            self.label.move(0, y)
        elif y > 400:
            self.label.move(x, 0)
        elif x < 0:
            self.label.move(400, y)
        elif y < 0:
            self.label.move(x, 400)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
