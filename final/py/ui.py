import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
#from img import imgwindow

from secondwindow import secondwindow

form_class = uic.loadUiType("mainwindow.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""
    def initUI(self):
        self.setupUi(self)
        self.practice.clicked.connect(self.button_second)
        self.explain.clicked.connect(self.explain_way)
    def explain_way(self):
        self.close()
        self.explain = explain_way()
        self.explain.exec()
        self.show()
    def button_second(self):
        #second = None
        self.close()
        self.second = secondwindow()
        self.second.exec()
        self.show()



explain_way = uic.loadUiType("explain_way.ui")[0]
class explain_way(QDialog,explain_way):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""
    def initUI(self):
        self.setupUi(self)
        self.ok.clicked.connect(self.back_home)

    def back_home(self):
        self.close()
        w = MyWindow()
        w.show()
        #w.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()