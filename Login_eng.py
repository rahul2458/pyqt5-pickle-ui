import pickle
import time

from PyQt5.uic.properties import QtWidgets

from main_details_abot_line import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QListWidgetItem, QInputDialog, qApp
from Login_engg import Ui_MainWindow
from PyQt5.QtCore import QPropertyAnimation, QPoint
import socket

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_3.setText("")

        # login button event
        self.ui.pushButton.clicked.connect(self.Login_fun)

    # login function and logic
    def Login_fun(self):

        if 'User' in self.ui.lineEdit.text() and 'user@123' in self.ui.lineEdit_2.text():
            self.ui.label_3.setText("Access")
            #self.ui = Ui_MainWindow()
            #self.ui.setupUi(self)
            self.ui.windows = MainWindow2()
            self.ui.windows.show()
            window.hide()
        elif 'Admin' in self.ui.lineEdit.text() and 'Admin@123456' in self.ui.lineEdit_2.text():
            self.ui.label_3.setText("Access")
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.windows = MainWindow2()
            self.ui.windows.show()
            window.hide()


        else:
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.label_3.setText('"Oops" Invalid user name and password')
            self.doShake()

    def doShake(self):
        self.doShakeWindow(self)

    def doShakeWindow(self, target):

        if hasattr(target, '_shake_animation'):
            return

        animation = QPropertyAnimation(target, b'pos', target)
        target._shake_animation = animation
        animation.finished.connect(lambda: delattr(target, '_shake_animation'))

        pos = target.pos()
        x, y = pos.x(), pos.y()

        animation.setDuration(50)
        animation.setLoopCount(5)
        animation.setKeyValueAt(0, QPoint(x, y))
        animation.setKeyValueAt(0.09, QPoint(x + 2, y - 2))
        animation.setKeyValueAt(0.18, QPoint(x + 4, y - 4))
        animation.setKeyValueAt(0.27, QPoint(x + 2, y - 6))
        animation.setKeyValueAt(0.36, QPoint(x + 0, y - 8))
        animation.setKeyValueAt(0.45, QPoint(x - 2, y - 10))
        animation.setKeyValueAt(0.54, QPoint(x - 4, y - 8))
        animation.setKeyValueAt(0.63, QPoint(x - 6, y - 6))
        animation.setKeyValueAt(0.72, QPoint(x - 8, y - 4))
        animation.setKeyValueAt(0.81, QPoint(x - 6, y - 2))
        animation.setKeyValueAt(0.90, QPoint(x - 4, y - 0))
        animation.setKeyValueAt(0.99, QPoint(x - 2, y + 2))
        animation.setEndValue(QPoint(x, y))

        animation.start(animation.DeleteWhenStopped)

    def keyPressEvent(self, e):
        # print("event", e)
        if e.key() == Qt.Key_Return:
            self.Login_fun()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.setAttribute(Qt.WA_TranslucentBackground)
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()

    sys.exit(app.exec_())
