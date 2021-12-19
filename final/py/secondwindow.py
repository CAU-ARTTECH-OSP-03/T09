import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from choose_level_bahnschrift import choose_level_bahnschrift
from choose_level_segoesc import choose_level_segoesc
from choose_level_arial import choose_level_arial
from choose_level_centurygothic import choose_level_centurygothic
from choose_level_girl import choose_level_girl
from choose_level_boopee import choose_level_boopee
form_secondwindow = uic.loadUiType("choose_font.ui")[0]
class secondwindow(QDialog,form_secondwindow):
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
        #self.b5.clicked.connect(self.chooselevel_b5)

    def chooselevel_b1(self):
        self.close()
        self.choose_level = choose_level_bahnschrift()
        self.choose_level.exec()
        self.show()
    def chooselevel_b2(self):
        self.close()
        self.choose_level = choose_level_segoesc()
        self.choose_level.exec()
        self.show()
    def chooselevel_b3(self):
        self.close()
        self.choose_level = choose_level_arial()
        self.choose_level.exec()
        self.show()
    def chooselevel_b4(self):
        self.close()
        self.choose_level = choose_level_centurygothic()
        self.choose_level.exec()
        self.show()
    def chooselevel_b5(self):
        self.close()
        self.choose_level = choose_level_boopee()
        self.choose_level.exec()
        self.show()





#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    win = secondwindow()
 #   app.exec_()