<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)

plt.plot(x, x, label='y=x')
plt.plot(x, x-1, label='y=x+b')
plt.plot(x, x**2, label='y=x2')
plt.plot(x, x**2 + x*1.5 + 1, label='y=a*x2+b*x+c')
plt.plot(x, x**3, label='y=x3')
#plt.plot(x, np.linalg.matrix_power(x, 1/2), label='y=sqrt(x)')
plt.plot(x, 1/x, label='y=k/x')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Simple plot')

plt.legend()
plt.show()
=======
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()


    def drawPoints(self, qp):

        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
>>>>>>> e338fe2ac520910bbfb645dbd85c25768a909071
