import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
#from img import imgwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

form_class = uic.loadUiType("mainwindow2.ui")[0]

class MyWindow2(QDialog, form_class):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""
    def initUI(self):
        self.setupUi(self)
        self.practice.clicked.connect(self.button_second)
        self.explain.clicked.connect(self.explain_way)
        self.graph.clicked.connect(self.graph_show)
    def explain_way(self):
        self.close()
        self.explain = explain_way()
        self.explain.exec()
        self.show()
    def button_second(self):
        #second = None
        self.close()
        from secondwindow import secondwindow
        self.second = secondwindow()
        self.second.exec()
        self.show()
    def graph_show(self):
        self.close()
        #from thirdwindow import thirdwindow
        self.third = thirdwindow()
        self.third.exec()
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
        w = MyWindow2()
        w.show()
        w.exec()
def graph(font,choose):#이미지 경로

    # txt 파일 없으면 생성
    #file_name = ("C:/Users/user/OPimage/"+font_name+ "_similarity.txt")
    font = "bahnschrift"
    choose = "alphabet"
    graph_file = "C:/Users/TOP/Desktop/opensource/"+font+"_"+choose+"similarity_graph.txt"
    from choose_level_bahnschrift import a
    from choose_level_bahnschrift import feedback_score

    #print('%.4f'%a)
    print(type(feedback_score))
    print(type(a))
    ab = str(a)
    a_ =open(graph_file,'a+')
    a_.write(ab)
    a_.write("\n")
    a_.close()

    r =open(graph_file,'r')
    lines=r.readlines() #한줄씩 읽기
    del lines[lines.index('\n')]
    print(lines)
    no_strip_lines=[] #줄바꿈 문자 제거한 txt 파일의 값[문자]를 넣는 리스트

    for i in range (len(lines)):
        no_strip_lines.append(lines[i].strip()) #줄바꿈 문자 제거
    print(no_strip_lines)
    r.close()
    remove_set = {''}
    no_blank = [i for i in no_strip_lines if i not in remove_set]
    print(no_blank)
    y = []
    for i in range(len(no_blank)):
        y.append(float(no_blank[i]))
    # y=[] # 그래프의 y값 모아두는 리스트
    # for i in range (len(no_strip_lines)):
    #     y.append(no_strip_lines[i])
    # print(y[1:])
    return y
global type
type = ""
form_thirdwindow = uic.loadUiType("choose_graph.ui")[0]
class thirdwindow(QDialog,form_thirdwindow):
    def __init__(self):
        super().__init__()
        self.thirdUI()
        self.show()
        self.third_text = ""
        #self.setWindowTitle(QtCore.FramelessWindowHint)
    def thirdUI(self):
        self.setupUi(self)
        #font = self.l_combo.currentText()
        self.ban.clicked.connect(self.goclassban)
        self.se.clicked.connect(self.goclassse)
        self.ar.clicked.connect(self.goclassar)
        self.go.clicked.connect(self.goclassgo)
    def goclassban(self):
        global type
        type = "ban"
        self.close()
        self.go2 = Ui_Dialog()
        self.go2.exec()
        self.show()
    def goclassse(self):
        global type
        type = "segoesc"
        self.close()
        self.go2 = Ui_Dialog()
        self.go2.exec()
        self.show()

    def goclassar(self):
        global type
        type = "arial"
        self.close()
        self.go2 = Ui_Dialog()
        self.go2.exec()
        self.show()
    def goclassgo(self):
        global type
        type = "gothic"
        self.close()
        self.go2 = Ui_Dialog()
        self.go2.exec()
        self.show()

form_sec_combo=uic.loadUiType("sec_combo.ui")[0]
class sec_comboboxban(QDialog,form_sec_combo):
    def __init__(self):
        super().__init__()
        self.gonsee()
        self.show()
        self.third_text = ""
        #self.setWindowTitle(QtCore.FramelessWindowHint)
    def gonsee(self):
        self.setupUi(self)
        #choose = self._combo.currentText()
        self.alpha.clicked.connect(self.gograph_ban_a)
        self.text.clicked.connect(self.gograph_ban_t)
    def gograph_ban_a(self):
        self.close()
        self.go3 = graph_show_ban_a()
        # self.go3.exec() #이거 안지우면 안됨
        self.show()
    def gograph_ban_t(self):
        self.close()
        self.go3 = graph_show_ban_t()
        self.go3.exec()
        self.show()

form_sec_combo=uic.loadUiType("sec_combo.ui")[0]
class sec_comboboxsese(QDialog,form_sec_combo):
    def __init__(self):
        super().__init__()
        self.gonsee()
        self.show()
        self.third_text = ""
        #self.setWindowTitle(QtCore.FramelessWindowHint)
    def gonsee(self):
        self.setupUi(self)
        #choose = self._combo.currentText()
        self.alpha.clicked.connect(self.gograph_se_a)
        self.text.clicked.connect(self.gograph_se_t)
    def gograph_se_a(self):
        self.close()
        self.go3 = graph_show_se_a()
        self.go3.exec()
        self.show()
    def gograph_se_t(self):
        self.close()
        self.go3 = graph_show_se_t()
        self.go3.exec()
        self.show()

form_sec_combo=uic.loadUiType("sec_combo.ui")[0]
class sec_comboboxmo(QDialog,form_sec_combo):
    def __init__(self):
        super().__init__()
        self.gonsee()
        self.show()
        self.third_text = ""
        #self.setWindowTitle(QtCore.FramelessWindowHint)
    def gonsee(self):
        self.setupUi(self)
        #choose = self._combo.currentText()
        self.alpha.clicked.connect(self.gograph_mo_a)

        self.text.clicked.connect(self.gograph_mo_t)
    def gograph_mo_a(self):
        self.close()
        self.go3 = graph_show_mo_a()
        self.go3.exec()
        self.show()
    def gograph_mo_t(self):
        self.close()
        self.go3 = graph_show_mo_t()
        self.go3.exec()
        self.show()

def graph_show_ban_a():
    #     self.Draw_ban_a()
    #     self.show()
    # def Draw_ban_a(self):
    class graph_show_ban_a_(QMainWindow):
        def __init__(self):
            super().__init__()
            self.main_widget = QWidget()
            self.setCentralWidget(self.main_widget)
            self.canvas = FigureCanvas(Figure(figsize=(4, 3)))
            vbox = QVBoxLayout(self.main_widget)
            vbox.addWidget(self.canvas)
            # 홈버튼
            btn1 = QPushButton("닫기", self)
            btn1.move(20, 20)
            # btn1.clicked.connect(QCoreApplication.instance().quit) => 이후 작성

            self.addToolBar(NavigationToolbar(self.canvas, self))
            self.ax = self.canvas.figure.subplots()
            y = graph("bahnshcrift", "alphabet")
            x = range(1, int(len(y)) + 1)
            # self.ax.plot(y,'-')
            self.ax.set_title("ban_alpha_similarity")
            self.ax.set_xlabel("num")
            self.ax.set_ylabel("similarity")
            self.ax.grid(True)

            self.ax.plot(x, y, 'b--o', lw=1)
            self.setWindowTitle('유사도 확인')
            self.setGeometry(300, 100, 600, 400)
            self.show()
    graph_show_ban_a_()

class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI(self)
        self.show()
    def initUI(self,Dialog):
        from choose_level_bahnschrift import ban_best_image_connect
        from choose_level_segoesc import segoesc_best_image_connect
        from choose_level_centurygothic import gothic_best_image_connect
        from choose_level_arial import arial_best_image_connect
        global type
        if (type == "ban"):
            pixmap = QPixmap(ban_best_image_connect)
        if (type == "segoesc"):
            pixmap = QPixmap(segoesc_best_image_connect)
        if (type == "arial"):
            pixmap = QPixmap(arial_best_image_connect)
        if (type == "gothic"):
            pixmap = QPixmap(gothic_best_image_connect)



        #Dialog.setObjectName("Dialog")
        Dialog.setStyleSheet("background:url(:/newPrefix/image.jfif)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 861, 641))
        self.label.setText("")
        self.label.setObjectName("label")

        self.label.setPixmap(QPixmap(pixmap))
        self.pushButton = QtWidgets.QPushButton(Dialog)

        self.pushButton.setGeometry(QtCore.QRect(20, 710, 861, 161))
        self.pushButton.setStyleSheet("background:rgba(254, 255, 185,150);\n"
"font: 18pt \"-다정\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 890, 131, 31))
        self.pushButton_2.setStyleSheet("background:rgba(254, 255, 185,150);\n"
"font: 14pt \"-다정\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.backhome)
        # self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.setGeometry(QtCore.QRect(480, 890, 131, 31))
        # self.pushButton_3.setStyleSheet("background:rgba(254, 255, 185,150);\n"
        #                                 "font: 14pt \"-다정\";")
        # self.pushButton_3.clicked.connect(self.bb)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # def bb(self):
    #     global ban_best_image_connect
    #     global type
    #     i = 1
    #     if (type == "alphabet"):
    #         ban_best_image_connect = "alphabetfeedback.png"
    #     elif (type == "sentence"):
    #         ban_best_image_connect = "sentencefeedback.png"

        # while i < k:
        #     # global type
        #     ban_best = "bahn_best_image" + str(i) + ".png"
        #
        #     if os.path.isfile(ban_best):
        #         i = i + 1
        #     else:
        #         type = "alphabet"
        #         ban_best_image.save("bahn_best_image" + str(i) + ".png")
        #
        #         ban_best_image_connect = "bahn_best_image" + str(i) + ".png"
        #         break

    def backhome(self):
        self.close()
        from ui2 import MyWindow2
        w = MyWindow2()
        w.show()
        w.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Best 이미지"))
        self.pushButton_2.setText(_translate("Dialog", "홈으로 돌아가기"))
        #self.pushButton_3.setText(_translate("Dialog", "Best 저장"))

#QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow2()
    win.show()
    app.exec_()