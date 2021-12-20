import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
#from img import imgwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
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
        self.graph.clicked.connect(self.graph_show)
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
        w = MyWindow()
        w.show()
        #w.exec()
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
        self.ar.clicked.connect(self.goclassmo)
    def goclassban(self):
        self.close()
        self.go2 = sec_comboboxban()
        self.go2.exec()
        self.show()
    def goclassse(self):
        self.close()
        self.go2 = sec_comboboxsese()
        self.go2.exec()
        self.show()

    def goclassmo(self):
        self.close()
        self.go2 = sec_comboboxmo()
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

class graph_show_ban_a(QMainWindow):
    def __init__(self):
        super().__init__()
    #     self.Draw_ban_a()
    #     self.show()
    # def Draw_ban_a(self):
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.canvas = FigureCanvas(Figure(figsize=(4, 3)))
        vbox = QVBoxLayout(self.main_widget)
        vbox.addWidget(self.canvas)
        #홈버튼
        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20)
        #btn1.clicked.connect(QCoreApplication.instance().quit) => 이후 작성

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()