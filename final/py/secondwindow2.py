import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore

form_secondwindow = uic.loadUiType("choose_font.ui")[0]
class secondwindow2(QDialog,form_secondwindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""
        #self.setWindowTitle(QtCore.FramelessWindowHint)
    def initUI(self):
        self.setupUi(self)
        self.b1.clicked.connect(self.chooselevel_b1)
        self.b2.clicked.connect(self.chooselevel_b2)
        self.b3.clicked.connect(self.chooselevel_b3)
        self.b4.clicked.connect(self.chooselevel_b4)
        self.home.clicked.connect(self.backhome)
    def backhome(self):
        self.close()
        from ui2 import MyWindow2
        w = MyWindow2()
        w.show()
        w.exec_()
    def chooselevel_b1(self):
        self.close()
        from choose_level_bahnschrift import choose_level_bahnschrift
        self.choose_level = choose_level_bahnschrift()
        self.choose_level.exec()
        self.show()
    def chooselevel_b2(self):
        self.close()
        from choose_level_segoesc import choose_level_segoesc
        self.choose_level = choose_level_segoesc()
        self.choose_level.exec()
        self.show()
    def chooselevel_b3(self):
        self.close()
        from choose_level_arial import choose_level_arial
        self.choose_level = choose_level_arial()
        self.choose_level.exec()
        self.show()
    def chooselevel_b4(self):
        self.close()
        from choose_level_centurygothic import choose_level_centurygothic
        self.choose_level = choose_level_centurygothic()
        self.choose_level.exec()
        self.show()





#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    win = secondwindow()
 #   app.exec_()