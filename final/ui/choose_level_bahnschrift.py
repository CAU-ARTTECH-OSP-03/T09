import sys
from pylab import plot, show,title, xlabel, ylabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image, ImageDraw, ImageFont
import cv2
from skimage.metrics import structural_similarity as compare_ssim
import time
import textwrap
import os
from choose_level_centurygothic import choose_level_centurygothic
from choose_level_segoesc import choose_level_segoesc
from choose_level_arial import choose_level_arial
import secondwindow
#from drawing_pad import CWidget, CView
import cv2
#from secondwindow import secondwindow
#from ui import MyWindow


global get_text
global fontimage_file_name_connect
global compare_file_name_connect
global fontimage_file_name_connect_alphabet
global compare_file_name_connect_alphabet
global feedback_image
global type
global feedback_image_alphabet_connect
global feedback_score

global one
global two
global three
global one_one
global two_two
global three_three
global feedback_image_sentence_connect
global sentence_one
global a
global ban_best_image_connect
ban_best_image_connect = ""
a = ""
sentence_one = ""
feedback_image_sentence_connect = ""
one_one = ""
two_two = ""
three_three = ""
one = ""
two = ""
three = ""

feedback_score = ""
type = "hello"
feedback_image_alphabet_connect = "hello"
compare_file_name_connect = "hello"
fontimage_file_name_connect = "hello"
compare_file_name_connect_alphabet = "hello"
fontimage_file_name_connect_alphabet = "hello"
feedback_image = "hello"
import sys
k = sys.maxsize
def sentence_feedback(char_level) :
    # 이미지 경로
    #imageA = r""+compare_file_name_connect+""
    #imageB = r""+feedback_image_sentence_connect+""

    # 이미지 읽어오기
    imageA_imread = cv2.imread(compare_file_name_connect)
    imageB_imread = cv2.imread(feedback_image_sentence_connect)

    # 결과 이미지 생성
    result_image = imageB_imread.copy()

    # 이미지 grayscale로 변경
    gray_imageA = cv2.cvtColor(imageA_imread, cv2.COLOR_BGR2GRAY)
    gray_imageB = cv2.cvtColor(imageB_imread, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray_imageA, gray_imageB, full=True)
    diff = (diff * 255).astype("uint8")
    global a
    #print(f"SIMILARITY : {score:.5f}")
    a = round(score, 4)
    global feedback_score

    # print("유사도에 따른 점수입니다")
    if (a > 0.7000):
        feedback_score = 5
        # print('5점 만점에 5점입니다')
    elif (a > 0.6700):
        feedback_score = 4
        # print('5점 만점에 4점입니다')
    elif (a > 0.6500):
        feedback_score = 3
        # print('5점 만점에 3점입니다')
    elif (a > 0.6300):
        feedback_score = 2
        # print('5점 만점에 2점입니다')
    else:
        feedback_score = 1
        # print('5점 만점에 1점입니다')
    graph_file = "C:/Users/TOP/Desktop/opensource/" + "bahnschrift" + "_" + "alphabet" + "similarity_graph.txt"
    # a_ = open(graph_file, 'a+')
    # a_.write(str(a))
    # a_.write("\n")
    # a_.close()

    #time.sleep(2)  # 다음 문구 표시를 위해 쉼

    while (True):  # 피드백 난도를 결정하는 부분
        #char_level = input("어느 정도로 정확한 피드백을 원하나요? \n 상(매우 정교함), 중(보통), 하(형태만 확인) 중 선택해주세요.")

        if char_level == "상":
            level = 70
            break

        elif char_level == "중":
            level = 200
            break

        elif char_level == "하":
            level = 250
            break

        else:
            print("다시 입력해 주세요")
    # 피드백 이미지
    for x in range(10, 850):  # 이미지의 가로 길이
        for y in range(130, 630):  # 이미지의 세로 길이
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
    drawing_is_down = 0
    drawing_is_up = 0
    for x in range(20, 840):  # 이미지의 가로 길이
        for y in range(20, 620):  # 이미지의 세로 길이
            if (x != 0) and (y != 0):
                if (gray_imageB[y - 1, x] == 223) and (gray_imageB[y, x] == 1):
                    drawing_is_down += 1
                elif (gray_imageB[y - 1, x] == 223) and (gray_imageB[y, x] == 1):
                    drawing_is_up += 1

    # drawing 이미지의 폭 피드백
    drawing_is_right = 0
    drawing_is_left = 0
    for y in range(0, 620):  # 이미지의 가로 길이
        for x in range(0, 840):  # 이미지의 세로 길이
            if (x != 0) and (y != 0):
                if (gray_imageB[y, x - 1] == 223) and (gray_imageB[y, x] == 1):
                    drawing_is_right += 1
                elif (gray_imageB[y, x - 1] == 223) and (gray_imageB[y, x] == 1):
                    drawing_is_left += 1

    if (abs(drawing_is_up - drawing_is_down) > abs(drawing_is_left - drawing_is_right)):
        global sentence_one
        if (drawing_is_up > drawing_is_down):
            sentence_one = "글씨가 위로 치우쳐 있는 경향이 있습니다.\n높이에 주의하며 글씨를 써주세요"
        else:
            sentence_one = "글씨가 아래로 치우쳐 있는 경향이 있습니다.\n높이에 주의하며 글씨를 써주세요"
    else:
        if (drawing_is_right > drawing_is_left):
            sentence_one = "글씨가 오른쪽으로 치우쳐 있는 경향이 있습니다.\n위치에 주의하며 글씨를 써주세요"
        else:
            sentence_one = "글씨가 왼쪽으로 치우쳐 있는 경향이 있습니다.\n위치에 주의하며 글씨를 써주세요"


    cv2.resize(result_image, (860, 640))
    cv2.imwrite("sentencefeedback.png", result_image)
    cv2.waitKey(0)
def alphabet_feedback(char_level) :
    # 이미지 경로
    imageA = cv2.imread(compare_file_name_connect)
    imageB = cv2.imread(feedback_image_alphabet_connect)

    # 이미지 읽어오기
    imageA_imread = cv2.imread(compare_file_name_connect)
    imageB_imread = cv2.imread(feedback_image_alphabet_connect)


    # 결과 이미지 생성
    result_image = imageB_imread.copy()

    # 이미지 grayscale로 변경
    gray_imageA = cv2.cvtColor(imageA_imread, cv2.COLOR_BGR2GRAY)
    gray_imageB = cv2.cvtColor(imageB_imread, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray_imageA, gray_imageB, full=True)
    diff = (diff * 255).astype("uint8")
    global a
    a = round(score, 4)
    global feedback_score
    #print("유사도에 따른 점수입니다")
    if (a > 0.7000):
        feedback_score = 5
        #print('5점 만점에 5점입니다')
    elif (a > 0.6700):
        feedback_score = 4
        #print('5점 만점에 4점입니다')
    elif (a > 0.6500):
        feedback_score = 3
        #print('5점 만점에 3점입니다')
    elif (a > 0.6300):
        feedback_score = 2
        #print('5점 만점에 2점입니다')
    else:
        feedback_score = 1
        #print('5점 만점에 1점입니다')

    #time.sleep(2)  # 다음 문구 표시를 위해 쉼

    while (True):  # 피드백 난도를 결정하는 부분
        #char_level = input("어느 정도로 정확한 피드백을 원하나요? \n 상(매우 정교함), 중(보통), 하(형태만 확인) 중 선택해주세요.")

        if char_level == "상":
            level = 70
            break

        elif char_level == "중":
            level = 200
            break

        elif char_level == "하":
            level = 250
            break

        else:
            print("다시 입력해 주세요")

    #print("이미지의 빨간색은 폰트와 어긋난 부분, 검은색은 폰트와 동일한 부분입니다.")
    #time.sleep(1)  # 앞의 문구 표시를 위해 쉼
    #print("빨간색 부분에 유의하면서 다시 한번 써보세요.")
    #time.sleep(2)  # 앞의 문구 표시를 위해 쉼

    for x in range(10, 850):  # 이미지의 가로 길이
        for y in range(130, 630):  # 이미지의 세로 길이
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경

    sq_w = 70
    sq_h = 145
    count = 0
    dic_wrongcount = {}

    dic_alpha_rocation = {}

    for i in range(7):  # 첫번째 줄 영역 표시
        for x in range(sq_w, sq_w + 90):  # for x in range((860 - w1) / 2.0,((860 - w1) / 2.0)+80):
            for y in range(sq_h, sq_h + 95):
                if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                    if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                        result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                        count = count + 1

        if (i == 0):
            dic_wrongcount['a'] = count
            dic_alpha_rocation['a'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
            #print(dic_alpha_rocation['a'])
        elif (i == 1):
            dic_wrongcount['b'] = count
            dic_alpha_rocation['b'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
            #print(dic_alpha_rocation['b'])
        elif (i == 2):
            dic_wrongcount['c'] = count
            dic_alpha_rocation['c'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
        elif (i == 3):
            dic_wrongcount['d'] = count
            dic_alpha_rocation['d'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
        elif (i == 4):
            dic_wrongcount['e'] = count
            dic_alpha_rocation['e'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
        elif (i == 5):
            dic_wrongcount['f'] = count
            dic_alpha_rocation['f'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
        elif (i == 6):
            dic_wrongcount['g'] = count
            dic_alpha_rocation['g'] = [sq_w, sq_w + 90, sq_h, sq_h + 95]
        count = 0
        sq_w = sq_w + 110

    sq_w = 35
    sq_h = 270

    for i in range(7):  # 두번째 줄 영역 표시
        if (i == 5):
            for x in range(sq_w + 5, sq_w + 95 + 5):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1



        elif (i == 6):
            for x in range(sq_w + 20, sq_w + 95 + 20):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1



        else:
            for x in range(sq_w, sq_w + 95):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1

        if (i == 0):
            dic_wrongcount['h'] = count
            dic_alpha_rocation['h'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
            #print(dic_alpha_rocation['h'])
        elif (i == 1):
            dic_wrongcount['i'] = count
            dic_alpha_rocation['i'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 2):
            dic_wrongcount['j'] = count
            dic_alpha_rocation['j'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 3):
            dic_wrongcount['k'] = count
            dic_alpha_rocation['k'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 4):
            dic_wrongcount['l'] = count
            dic_alpha_rocation['l'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 5):
            dic_wrongcount['m'] = count
            dic_alpha_rocation['m'] = [sq_w + 5, sq_w + 95 + 5, sq_h, sq_h + 87]
        elif (i == 6):
            dic_wrongcount['n'] = count
            dic_alpha_rocation['n'] = [sq_w + 20, sq_w + 95 + 20, sq_h, sq_h + 87]
        count = 0
        sq_w = sq_w + 110

    sq_w = 60
    sq_h = 385
    count = 0

    for i in range(7):  # 세번째 줄 영역 표시
        if (i > 4):
            for x in range(sq_w - 10, sq_w + 85):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1


        else:
            for x in range(sq_w, sq_w + 95):  # for x in range((860 - w3) / 2.0,((860 - w3) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1

        if (i == 0):
            dic_wrongcount['o'] = count
            dic_alpha_rocation['o'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 1):
            dic_wrongcount['p'] = count
            dic_alpha_rocation['p'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 2):
            dic_wrongcount['q'] = count
            dic_alpha_rocation['q'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 3):
            dic_wrongcount['r'] = count
            dic_alpha_rocation['r'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 4):
            dic_wrongcount['s'] = count
            dic_alpha_rocation['s'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 5):
            dic_wrongcount['t'] = count
            dic_alpha_rocation['t'] = [sq_w - 10, sq_w + 85, sq_h, sq_h + 87]
        elif (i == 6):
            dic_wrongcount['u'] = count
            dic_alpha_rocation['u'] = [sq_w - 10, sq_w + 85, sq_h, sq_h + 87]
        count = 0
        sq_w = sq_w + 110

    sq_w = 160
    sq_h = 515

    for i in range(5):  # 네번 째 줄 영역 표시
        if (i == 1):
            for x in range(sq_w + 10, sq_w + 95 + 10):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1

        elif (i > 1):
            for x in range(sq_w + 20, sq_w + 95 + 20):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1

        else:
            for x in range(sq_w, sq_w + 95):  # for x in range((860 - w2) / 2.0,((860 - w2) / 2.0)+80):
                for y in range(sq_h, sq_h + 87):
                    if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                        if gray_imageA[y, x] - (
                        gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                            result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                            count = count + 1

        if (i == 0):
            dic_wrongcount['v'] = count
            dic_alpha_rocation['v'] = [sq_w, sq_w + 95, sq_h, sq_h + 87]
        elif (i == 1):
            dic_wrongcount['w'] = count
            dic_alpha_rocation['w'] = [sq_w + 10, sq_w + 10 + 95, sq_h, sq_h + 87]
        elif (i == 2):
            dic_wrongcount['x'] = count
            dic_alpha_rocation['x'] = [sq_w + 20, sq_w + 20 + 95, sq_h, sq_h + 87]
        elif (i == 3):
            dic_wrongcount['y'] = count
            dic_alpha_rocation['y'] = [sq_w + 20, sq_w + 20 + 95, sq_h, sq_h + 87]
        elif (i == 4):
            dic_wrongcount['z'] = count
            dic_alpha_rocation['z'] = [sq_w + 20, sq_w + 20 + 95, sq_h, sq_h + 87]
        count = 0
        sq_w = sq_w + 110
    _alpha_value = 2
    __alpha_value = 1
    ___alpha_value = 0

    list_wrongcont = dic_wrongcount.values()
    for i in list_wrongcont:
        if (i > _alpha_value):
            _alpha_value = i
        elif (__alpha_value < i < _alpha_value):
            __alpha_value = i
        elif (___alpha_value < i < __alpha_value):
            ___alpha_value = i

    dic_wrongcount_reverse = {v: k for k, v in dic_wrongcount.items()}
    global one
    global two
    global three
    one = dic_wrongcount_reverse[_alpha_value]
    two = dic_wrongcount_reverse[__alpha_value]
    three = dic_wrongcount_reverse[___alpha_value]

    #print("가장 오류가 많은 알파벳은 " +
    #      dic_wrongcount_reverse[_alpha_value], dic_wrongcount_reverse[__alpha_value],
    #      dic_wrongcount_reverse[___alpha_value] + "입니다.")

    _alpha_valueList = dic_alpha_rocation[dic_wrongcount_reverse[_alpha_value]]
    __alpha_valueList = dic_alpha_rocation[dic_wrongcount_reverse[__alpha_value]]
    ___alpha_valueList = dic_alpha_rocation[dic_wrongcount_reverse[___alpha_value]]

    # _alpha_vlaue 문장 피드백
    dic_alpha_value = {}
    dic__alpha_value = {}
    dic___alpha_value = {}

    for x in range(int(_alpha_valueList[0]),
                   int(_alpha_valueList[0] + (_alpha_valueList[1] - _alpha_valueList[0]) / 2)):
        for y in range(int(_alpha_valueList[2] + (_alpha_valueList[3] - _alpha_valueList[2]) / 2), _alpha_valueList[3]):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic_alpha_value['왼쪽 아래'] = count
    count = 0

    for x in range(int(_alpha_valueList[0] + (_alpha_valueList[1] - _alpha_valueList[0]) / 2), _alpha_valueList[1]):
        for y in range(int(_alpha_valueList[2] + (_alpha_valueList[3] - _alpha_valueList[2]) / 2), _alpha_valueList[3]):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic_alpha_value['오른쪽 아래'] = count
    count = 0

    for x in range(int(_alpha_valueList[0]),
                   int(_alpha_valueList[0] + (_alpha_valueList[1] - _alpha_valueList[0]) / 2)):
        for y in range(int(_alpha_valueList[2]),
                       int(_alpha_valueList[2] + (_alpha_valueList[3] - _alpha_valueList[2]) / 2)):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic_alpha_value['왼쪽 위'] = count
    count = 0

    for x in range(int(_alpha_valueList[0] + (_alpha_valueList[1] - _alpha_valueList[0]) / 2), _alpha_valueList[1]):
        for y in range(int(_alpha_valueList[2]),
                       int(_alpha_valueList[2] + (_alpha_valueList[3] - _alpha_valueList[2]) / 2)):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic_alpha_value['오른쪽 위'] = count
    count = 0

    #print(dic_alpha_value)
    dic_alpha_value_reverse = {v: k for k, v in dic_alpha_value.items()}
    list_alpha_value = dic_alpha_value.values()
    alpha_in_red = 0
    for i in list_alpha_value:
        if (i > alpha_in_red):
            alpha_in_red = i
    global one_one
    one_one = dic_wrongcount_reverse[_alpha_value] + "의 " + dic_alpha_value_reverse[alpha_in_red] + "부분에 유의하며 써주세요."

    # __alpha_vlaue 문장 피드백
    for x in range(int(__alpha_valueList[0]),
                   int(__alpha_valueList[0] + (__alpha_valueList[1] - __alpha_valueList[0]) / 2)):
        for y in range(int(__alpha_valueList[2] + (__alpha_valueList[3] - __alpha_valueList[2]) / 2),
                       __alpha_valueList[3]):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic__alpha_value['왼쪽 아래'] = count
    count = 0

    for x in range(int(__alpha_valueList[0] + (__alpha_valueList[1] - __alpha_valueList[0]) / 2), __alpha_valueList[1]):
        for y in range(int(__alpha_valueList[2] + (__alpha_valueList[3] - __alpha_valueList[2]) / 2),
                       __alpha_valueList[3]):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic__alpha_value['오른쪽 아래'] = count
    count = 0

    for x in range(int(__alpha_valueList[0]),
                   int(__alpha_valueList[0] + (__alpha_valueList[1] - __alpha_valueList[0]) / 2)):
        for y in range(int(__alpha_valueList[2]),
                       int(__alpha_valueList[2] + (__alpha_valueList[3] - __alpha_valueList[2]) / 2)):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic__alpha_value['왼쪽 위'] = count
    count = 0

    for x in range(int(__alpha_valueList[0] + (__alpha_valueList[1] - __alpha_valueList[0]) / 2), __alpha_valueList[1]):
        for y in range(int(__alpha_valueList[2]),
                       int(__alpha_valueList[2] + (__alpha_valueList[3] - __alpha_valueList[2]) / 2)):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 225)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic__alpha_value['오른쪽 위'] = count
    count = 0

    dic__alpha_value_reverse = {v: k for k, v in dic__alpha_value.items()}
    list__alpha_value = dic__alpha_value.values()
    alpha__in_red = 0
    for i in list__alpha_value:
        if (i > alpha__in_red):
            alpha__in_red = i

    #print(dic__alpha_value)
    global two_two
    two_two = dic_wrongcount_reverse[__alpha_value] + "의 " + dic__alpha_value_reverse[alpha__in_red] + "부분에 유의하며 써주세요."

    # ___alpha_vlaue 문장 피드백
    for x in range(int(___alpha_valueList[0]),
                   int(___alpha_valueList[0] + (___alpha_valueList[1] - ___alpha_valueList[0]) / 2)):
        for y in range(int(___alpha_valueList[2] + (___alpha_valueList[3] - ___alpha_valueList[2]) / 2),
                       ___alpha_valueList[3]):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 225)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic___alpha_value['왼쪽 아래'] = count
    count = 0

    for x in range(int(___alpha_valueList[0] + (___alpha_valueList[1] - ___alpha_valueList[0]) / 2),
                   ___alpha_valueList[1]):
        for y in range(int(___alpha_valueList[2] + (___alpha_valueList[3] - ___alpha_valueList[2]) / 2),
                       ___alpha_valueList[3]):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic___alpha_value['오른쪽 아래'] = count
    count = 0

    for x in range(int(___alpha_valueList[0]),
                   int(___alpha_valueList[0] + (___alpha_valueList[1] - ___alpha_valueList[0]) / 2)):
        for y in range(int(___alpha_valueList[2]),
                       int(___alpha_valueList[2] + (___alpha_valueList[3] - ___alpha_valueList[2]) / 2)):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic___alpha_value['왼쪽 위'] = count
    count = 0

    for x in range(int(___alpha_valueList[0] + (___alpha_valueList[1] - ___alpha_valueList[0]) / 2),
                   ___alpha_valueList[1]):
        for y in range(int(___alpha_valueList[2]),
                       int(___alpha_valueList[2] + (___alpha_valueList[3] - ___alpha_valueList[2]) / 2)):
            if gray_imageA[y, x] > gray_imageB[y, x]:  # 글씨 가이드라인 제외하기
                if gray_imageA[y, x] - (gray_imageB[y, x]) > level:  # 사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                    result_image[y, x] = (0, 0, 255)  # 픽셀을 빨간색으로 변경
                    count = count + 1
    dic___alpha_value['오른쪽 위'] = count
    count = 0
    #print(dic___alpha_value)

    dic___alpha_value_reverse = {v: k for k, v in dic___alpha_value.items()}
    list___alpha_value = dic___alpha_value.values()
    alpha___in_red = 0
    for i in list___alpha_value:
        if (i > alpha___in_red):
            alpha___in_red = i
    global three_three
    three_three = dic_wrongcount_reverse[___alpha_value] + "의 " + dic___alpha_value_reverse[alpha___in_red] + "부분에 유의하며 써주세요."
    cv2.resize(result_image, (860, 640))
    cv2.imwrite("alphabetfeedback.png",result_image)
    cv2.waitKey(0)
def make_font_image_alphabet_compare(font_name):
    global compare_file_name_connect
    im = Image.open(
        "C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/whitewithgrid.jpg")  # 배경이미지불러오기

    if font_name.upper() == font_name.lower():  # 폰트이름이전체한글이고, 한글폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70)
        row0 = font_name
        row1 = 'a  b  c  d  e  f  g'
        row2 = 'h  i  j  k  l  m  n'
        row3 = 'o  p  q  r  s  t  u'
        row4 = 'v  w  x  y  z'
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(row1, font=myfont1)
        w2, h2 = draw.textsize(row2, font=myfont1)
        w3, h3 = draw.textsize(row3, font=myfont1)
        w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40), fill='black')
        draw.text(((860 - w1) / 2.0, 125), textwrap.fill(write, 20),
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70), fill='black')
        i = 1
        compare_file_name = font_name + "_original_custom" + i + ".png"
        if os.path.isfile(compare_file_name):
            im.save(font_name + "_original_custom" + (i + 1) + ".png")
        else:
            im.save(font_name + "_original_custom" + i + ".png")
    else:  # 폰트이름이전체 영어이고, 영어폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70)
        row0 = font_name
        row1 = 'a  b  c  d  e  f  g'
        row2 = 'h  i  j  k  l  m  n'
        row3 = 'o  p  q  r  s  t  u'
        row4 = 'v  w  x  y  z'
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(row1, font=myfont1)
        w2, h2 = draw.textsize(row2, font=myfont1)
        w3, h3 = draw.textsize(row3, font=myfont1)
        w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40), fill='black')
        draw.text(((860-w1)/2.0, 125), row1 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill='black')
        draw.text(((860-w2)/2.0, 245), row2 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill='black')
        draw.text(((860-w3)/2.0, 365), row3,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill='black')
        draw.text(((860-w4)/2.0, 485), row4,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill='black')
        while(True):
            im.save(font_name + "_original_custom_alphabet.png")
            compare_file_name_connect = font_name + "_original_custom_alphabet.png"
            break
def make_font_image_alphabet(font_name):
    global fontimage_file_name_connect
    im = Image.open(
        "C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/whitewithgrid.jpg")  # 배경이미지불러오기

    if font_name.upper() == font_name.lower():  # 폰트이름이전체한글이고, 한글폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70)
        row0 = font_name
        row1 = 'a  b  c  d  e  f  g'
        row2 = 'h  i  j  k  l  m  n'
        row3 = 'o  p  q  r  s  t  u'
        row4 = 'v  w  x  y  z'
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(row1, font=myfont1)
        w2, h2 = draw.textsize(row2, font=myfont1)
        w3, h3 = draw.textsize(row3, font=myfont1)
        w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40), fill='black')
        draw.text(((860 - w1) / 2.0, 125), textwrap.fill(write, 20),
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70), fill=(224, 224, 224))
        im.save(font_name + "fontimage_custom_alphabet.png")

        fontimage_file_name_connect_alphabet = font_name + "fontimage_custom_alphabet.png"
    else:  # 폰트이름이전체 영어이고, 영어폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70)
        row0 = font_name
        row1 = 'a  b  c  d  e  f  g'
        row2 = 'h  i  j  k  l  m  n'
        row3 = 'o  p  q  r  s  t  u'
        row4 = 'v  w  x  y  z'
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(textwrap.fill(row1, 20), font=myfont1)
        w2, h2 = draw.textsize(row2, font=myfont1)
        w3, h3 = draw.textsize(row3, font=myfont1)
        w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40), fill='black')
        draw.text(((860-w1)/2.0, 125), row1 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill=(224,224,224))
        draw.text(((860-w2)/2.0, 245), row2 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill=(224,224,224))
        draw.text(((860-w3)/2.0, 365), row3,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill=(224,224,224))
        draw.text(((860-w4)/2.0, 485), row4,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill=(224,224,224))
        while (True):
            im.save(font_name + "_fontimage_custom_alphabet.png")
            fontimage_file_name_connect = font_name + "_fontimage_custom_alphabet.png"
            break
def make_font_image_compare(font_name,write):
    im = Image.open(
        "C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/whitewithgrid.jpg")  # 배경이미지불러오기
    global compare_file_name_connect
    if font_name.upper() == font_name.lower():  # 폰트이름이전체한글이고, 한글폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70)
        row0 = font_name
        w0, h0 = draw.textsize(row0, font=myfont0)

        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40), fill='black')
        draw.text(((860 - w1) / 2.0, 125), textwrap.fill(write, 20),
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70), fill='black')
        i = 1
        compare_file_name = font_name + "_original_custom" + i + ".png"
        if os.path.isfile(compare_file_name):
            im.save(font_name + "_original_custom" + (i + 1) + ".png")
        else:
            im.save(font_name + "_original_custom" + i + ".png")
    else:  # 폰트이름이전체 영어이고, 영어폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70)
        row0 = font_name
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(textwrap.fill(write, 20), font=myfont1)
        #w2, h2 = draw.textsize(row2, font=myfont1)
        #w3, h3 = draw.textsize(row3, font=myfont1)
        #w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40), fill='black')
        draw.text(((860 - w1) / 2.0, 125), textwrap.fill(write, 20),
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill='black')
        i = 1
        while i < k:
            compare_file_name = font_name + "_original_custom" + str(i) + ".png"

            if os.path.isfile(compare_file_name):
                i = i + 1
            else:
                im.save(font_name + "_original_custom" + str(i) + ".png")

                compare_file_name_connect = font_name + "_original_custom" + str(i) + ".png"
                break
def make_font_image(font_name,write):
    im = Image.open(
        "C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/whitewithgrid.jpg")  # 배경이미지불러오기
    global fontimage_file_name_connect
    if font_name.upper() == font_name.lower():  # 폰트이름이전체한글이고, 한글폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70)
        row0 = font_name
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(textwrap.fill(write, 20), font=myfont1)
        #w2, h2 = draw.textsize(row2, font=myfont1)
        #w3, h3 = draw.textsize(row3, font=myfont1)
        #w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40), fill='black')
        draw.text(((860 - w1) / 2.0, 125), textwrap.fill(write, 20),
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 70), fill=(224, 224, 224))
        i = 1
        fontimage_file_name = font_name + "fontimage_custom" + str(i) + ".png"

        if os.path.isfile(fontimage_file_name):
            im.save(font_name + "fontimage_custom" + str(i + 1) + ".png")

            fontimage_file_name_connect = font_name + "fontimage_custom" + str(i + 1) + ".png"
        else:
            im.save(font_name + "fontimage_custom" + str(i) + ".png")

            fontimage_file_name_connect = font_name + "fontimage_custom" + str(i) + ".png"
    else:  # 폰트이름이전체 영어이고, 영어폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70)
        row0 = font_name
        w0, h0 = draw.textsize(row0, font=myfont0)
        w1, h1 = draw.textsize(textwrap.fill(write, 20), font=myfont1)
        #w2, h2 = draw.textsize(row2, font=myfont1)
        #w3, h3 = draw.textsize(row3, font=myfont1)
        #w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860 - w0) / 2.0, 50), font_name,
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40), fill='black')
        draw.text(((860 - w1) / 2.0, 125), textwrap.fill(write, 20),
                  font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 70), fill=(224, 224, 224))
        i = 1
        while i < k:

            fontimage_file_name = font_name + "fontimage_custom" + str(i) + ".png"

            if os.path.isfile(fontimage_file_name):
                i = i + 1
            else:
                im.save(font_name + "fontimage_custom" + str(i) + ".png")

                fontimage_file_name_connect = font_name + "fontimage_custom" + str(i) + ".png"
                break

form_choose_level = uic.loadUiType("choose_level.ui")[0]
class choose_level_bahnschrift(QDialog,form_choose_level):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""
        #self.setWindowTitle(QtCore.FramelessWindowHint)
    def initUI(self):
        self.setupUi(self)
        self.alphabet.clicked.connect(self.choose_alphabet)
        self.sentence.clicked.connect(self.choose_sentence)

        self.home.clicked.connect(self.backhome)

    def backhome(self):
        self.close()
        from ui2 import MyWindow2
        w = MyWindow2()
        w.show()
        w.exec_()
    def choose_alphabet(self):
        global type
        type = "alphabet"
        self.close()
        make_font_image_alphabet_compare("bahnschrift")
        make_font_image_alphabet("bahnschrift")
        w = CWidget()
        w.show()
        w.exec_()

    def choose_sentence(self):
        global type
        type = "sentence"
        self.close()
        w = choose_sentence()
        w.show()
        w.exec_()
import random
def random_text():
    list_text = ["No pain, No gain.", "Time is gold.", "From zero to hero.", "Desperate triumphs over luck",
                    "One day or day one. It's your choice.", "Believe you can and you're halfway there.",
                     "All we have is now.", "Don't let yesterday take up too much of today.",
                     "Things end, people change, And life goes on.",
                     "You get what you work for, not what you wish for.",
                     "Although world is full of suffering, It is full also of overcoming of it.",
                     "You can do it!", "All we have is now."]

    return list_text[random.randint(1, len(list_text))]


form_choose_sentence = uic.loadUiType("choose_sentence.ui")[0]
class choose_sentence(QDialog,form_choose_sentence):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.second_text = ""

    def initUI(self):
        self.setupUi(self)
        self.own_write.clicked.connect(self.draw_own_write_image)
        self.famous.clicked.connect(self.famous_saying_text)

        self.home.clicked.connect(self.backhome)


    def backhome(self):
        self.close()
        from ui2 import MyWindow2
        w = MyWindow2()
        w.show()
        w.exec_()
    def draw_own_write_image(self):
        self.close()
        w = write_sentence()
        w.show()
        w.exec_()

    def famous_saying_text(self):
        self.close()
        get_text = random_text()
        make_font_image_compare("bahnschrift", get_text)
        make_font_image("bahnschrift", get_text)
        w = CWidget()
        w.show()
        w.exec_()


form_write_sentence = uic.loadUiType("write_sentence.ui")[0]
class write_famous_sentence(QDialog,form_write_sentence):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.ok.clicked.connect(self.drawing_famous_pad)


    def drawing_famous_pad(self):
        self.close()
        get_text = random_text()
        make_font_image_compare("bahnschrift", get_text)
        make_font_image("bahnschrift", get_text)
        w = CWidget()
        w.show()
        w.exec_()

form_write_sentence = uic.loadUiType("write_sentence.ui")[0]
class write_sentence(QDialog,form_write_sentence):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.ok.clicked.connect(self.drawing_pad)

        self.home.clicked.connect(self.backhome)

    def backhome(self):
        self.close()
        from ui2 import MyWindow2
        w = MyWindow2()
        w.show()
        w.exec_()

    def drawing_pad(self):
        self.close()
        get_text = self.TEXT.toPlainText()
        make_font_image_compare("bahnschrift", get_text)
        make_font_image("bahnschrift", get_text)
        w = CWidget()
        w.show()
        w.exec_()
choose_feedback_level = uic.loadUiType("choose_feedback_level.ui")[0]
class choose_feedback_level(QDialog,choose_feedback_level):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.setupUi(self)
        self.high.clicked.connect(self.feedback_high)
        self.middle.clicked.connect(self.feedback_middle)
        self.low.clicked.connect(self.feedback_low)

    def feedback_high(self):
        global type
        if (type == "alphabet"):
            self.close()
            alphabet_feedback("상")
            type = "alphabet"
            w = Ui_Dialog()
            w.show()
            w.exec_()
        elif (type == "sentence"):
            self.close()
            sentence_feedback("상")
            type = "sentence"
            w = Ui_Dialog()
            w.show()
            w.exec_()

    def feedback_middle(self):
        global type
        if (type == "alphabet"):
            self.close()
            alphabet_feedback("중")
            type = "alphabet"
            w = Ui_Dialog()
            w.show()
            w.exec_()
        elif (type == "sentence"):
            self.close()
            sentence_feedback("중")
            type = "sentence"
            w = Ui_Dialog()
            w.show()
            w.exec_()

    def feedback_low(self):
        global type
        if (type == "alphabet"):
            self.close()
            alphabet_feedback("하")
            type = "alphabet"
            w = Ui_Dialog()
            w.show()
            w.exec_()
        elif (type == "sentence"):
            self.close()
            sentence_feedback("하")
            type = "sentence"
            w = Ui_Dialog()
            w.show()
            w.exec_()


class Ui_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI(self)
        self.show()
    def initUI(self,Dialog):
        global type
        #Dialog.setObjectName("Dialog")
        Dialog.setStyleSheet("background:url(:/newPrefix/image.jfif)")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 861, 641))
        self.label.setText("")
        self.label.setObjectName("label")
        if (type == "alphabet"):
            pixmap = QPixmap("alphabetfeedback.png")
        elif (type == "sentence"):
            pixmap = QPixmap("sentencefeedback.png")

        self.label.setPixmap(QPixmap(pixmap))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        if (type == "alphabet"):
            self.pushButton.setGeometry(QtCore.QRect(20, 710, 861, 161))
        elif (type == "sentence"):
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
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QtCore.QRect(380, 920, 131, 31))
        self.pushButton_3.setStyleSheet("background:rgba(254, 255, 185,150);\n"
                                        "font: 14pt \"-다정\";")
        self.pushButton_3.clicked.connect(self.bb)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def bb(self):
        global ban_best_image_connect
        global feedback_image_alphabet_connect
        global feedback_image_sentence_connect
        global type
        i = 1
        if (type == "alphabet"):
            ban_best_image_connect = feedback_image_alphabet_connect
        elif (type == "sentence"):
            ban_best_image_connect = feedback_image_sentence_connect

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
        if (type == "alphabet"):
            self.pushButton.setText(_translate("Dialog", "빨간색 부분은 폰트에서 벗어난 부분입니다. 유의하여 다시 작성해 보세요. \n"
" 유사도에 따른 점수는 5점 만점에 "+str(feedback_score)+"점입니다. \n"
" 가장 많이 벗어난 알파벳은"+one+" "+two+" "+three+" "+"입니다. \n"+one_one+"\n"+two_two+"\n"+three_three))
        elif (type == "sentence"):
            self.pushButton.setText(_translate("Dialog", "빨간색 부분은 폰트에서 벗어난 부분입니다. 유의하여 다시 작성해 보세요. \n"
                                                         " 유사도에 따른 점수는 5점 만점에 " + str(feedback_score) + "점입니다. \n"
                                                                                                        +sentence_one ))
        self.pushButton_2.setText(_translate("Dialog", "홈으로 돌아가기"))
        self.pushButton_3.setText(_translate("Dialog", "Best 저장"))

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class CWidget(QDialog):
    def __init__(self):

        super().__init__()

        # 전체 폼 박스
        formbox = QHBoxLayout()
        self.setLayout(formbox)

        # 좌, 우 레이아웃박스
        left = QVBoxLayout()
        right = QVBoxLayout()

        # 그룹박스1 생성 및 좌 레이아웃 배치
        gb = QGroupBox('그리기 종류')
        left.addWidget(gb)

        # 그룹박스1 에서 사용할 레이아웃
        box = QVBoxLayout()
        gb.setLayout(box)

        # 그룹박스 1 의 라디오 버튼 배치
        text = ['line', 'Curve','Rectange', 'Ellipse']
        self.radiobtns = []

        for i in range(len(text)):
            self.radiobtns.append(QRadioButton(text[i], self))
            self.radiobtns[i].clicked.connect(self.radioClicked)
            box.addWidget(self.radiobtns[i])

        self.radiobtns[0].setChecked(True)
        self.drawType = 0

        # 그룹박스2
        gb = QGroupBox('펜 설정')
        left.addWidget(gb)

        grid = QGridLayout()
        gb.setLayout(grid)

        label = QLabel('선굵기')
        grid.addWidget(label, 0, 0)

        self.combo = QComboBox()
        grid.addWidget(self.combo, 0, 1)

        for i in range(1, 21):
            self.combo.addItem(str(i))

        label = QLabel('선색상')
        grid.addWidget(label, 1, 0)

        self.pencolor = QColor(0, 0, 0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet('background-color: rgb(0,0,0)')
        self.penbtn.clicked.connect(self.showColorDlg)
        grid.addWidget(self.penbtn, 1, 1)

        # 그룹박스3
        gb = QGroupBox('붓 설정')
        left.addWidget(gb)

        hbox = QHBoxLayout()
        gb.setLayout(hbox)

        #label = QLabel('붓색상')
        hbox.addWidget(label)

        self.brushcolor = QColor(255, 255, 255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet('background-color: rgb(255,255,255)')
        self.brushbtn.clicked.connect(self.showColorDlg)
        hbox.addWidget(self.brushbtn)

        # 그룹박스4
        gb = QGroupBox('지우개')
        left.addWidget(gb)

        hbox = QHBoxLayout()
        gb.setLayout(hbox)

        self.checkbox = QCheckBox('지우개 동작')
        self.checkbox.stateChanged.connect(self.checkClicked)
        hbox.addWidget(self.checkbox)

        left.addStretch(1)

        #그룹박스5
        def image_save():
            img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
            i = 1
            global feedback_image_alphabet_connect
            global feedback_image_sentence_connect
            global type
            if (type == "alphabet"):
                while i < k:
                    # global type
                    feedback_image_alphabet = "bahn_feedback_alphabet" + str(i) + ".png"

                    if os.path.isfile(feedback_image_alphabet):
                        i = i + 1
                    else:
                        type = "alphabet"
                        img.save("bahn_feedback_alphabet" + str(i) + ".png")

                        feedback_image_alphabet_connect = "bahn_feedback_alphabet" + str(i) + ".png"
                        break
            elif (type == "sentence"):
                while i < k:
                    # global type
                    feedback_image_sentence = "bahn_feedback_sentence" + str(i) + ".png"

                    if os.path.isfile(feedback_image_sentence):
                        i = i + 1
                    else:
                        type = "sentence"
                        img.save("bahn_feedback_sentence" + str(i) + ".png")
                        feedback_image_sentence_connect = "bahn_feedback_sentence" + str(i) + ".png"
                        break

        gb = QGroupBox('')
        left.addWidget(gb)

        hbox = QHBoxLayout()
        gb.setLayout(hbox)

        save = QPushButton('저장')
        hbox.addWidget(save)
        save.clicked.connect(image_save)

        #그룹박스6
        gb = QGroupBox('')
        left.addWidget(gb)

        hbox = QHBoxLayout()
        gb.setLayout(hbox)

        feedback = QPushButton('피드백')
        hbox.addWidget(feedback)
        feedback.clicked.connect(self.choose_feedback_level)

        # 우 레이아웃 박스에 그래픽 뷰 추가
        self.view = CView(self)
        right.addWidget(self.view)

        # 전체 폼박스에 좌우 박스 배치
        formbox.addLayout(left)
        formbox.addLayout(right)

        formbox.setStretchFactor(left, 0)
        formbox.setStretchFactor(right, 1)

        self.setGeometry(100, 100, 997, 664)

    def choose_feedback_level(self):
        self.close()
        w = choose_feedback_level()
        w.show()
        w.exec()

    def radioClicked(self):
        for i in range(len(self.radiobtns)):
            if self.radiobtns[i].isChecked():
                self.drawType = i
                break

    def checkClicked(self):
        pass

    def showColorDlg(self):

        # 색상 대화상자 생성
        color = QColorDialog.getColor()

        sender = self.sender()

        # 색상이 유효한 값이면 참, QFrame에 색 적용
        if sender == self.penbtn and color.isValid():
            self.pencolor = color
            self.penbtn.setStyleSheet('background-color: {}'.format(color.name()))
        else:
            self.brushcolor = color
            self.brushbtn.setStyleSheet('background-color: {}'.format(color.name()))


# QGraphicsView display QGraphicsScene

class CView(QGraphicsView):

    def __init__(self, parent):

        super().__init__(parent)
        self.pixmap = QPixmap()
        self.pixmap.load(fontimage_file_name_connect)
        self.scene = QGraphicsScene()
        self.scene.addPixmap(self.pixmap)
        self.setScene(self.scene)

        self.items = []

        self.start = QPointF()
        self.end = QPointF()

        self.setRenderHint(QPainter.HighQualityAntialiasing)

    def moveEvent(self, e):
        rect = QRectF(self.rect())
        rect.adjust(0, 0, -2, -2)

        self.scene.setSceneRect(rect)

    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            # 시작점 저장
            self.start = e.pos()
            self.end = e.pos()

    def mouseMoveEvent(self, e):

        # e.buttons()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴
        if e.buttons() & Qt.LeftButton:

            self.end = e.pos()

            if self.parent().checkbox.isChecked():
                pen = QPen(QColor(255, 255, 255), 10)
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
                self.start = e.pos()
                return None

            pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())

            # 직선 그리기
            if self.parent().drawType == 0:

                # 장면에 그려진 이전 선을 제거
                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del (self.items[-1])

                    # 현재 선 추가
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                self.items.append(self.scene.addLine(line, pen))

            # 곡선 그리기
            if self.parent().drawType == 1:
                # Path 이용
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)

                # Line 이용
                # line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                # self.scene.addLine(line, pen)

                # 시작점을 다시 기존 끝점으로
                self.start = e.pos()

            # 사각형 그리기
            if self.parent().drawType == 2:
                brush = QBrush(self.parent().brushcolor)

                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del (self.items[-1])

                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addRect(rect, pen, brush))

            # 원 그리기
            if self.parent().drawType == 3:
                brush = QBrush(self.parent().brushcolor)

                if len(self.items) > 0:
                    self.scene.removeItem(self.items[-1])
                    del (self.items[-1])

                rect = QRectF(self.start, self.end)
                self.items.append(self.scene.addEllipse(rect, pen, brush))

    def mouseReleaseEvent(self, e):

        if e.button() == Qt.LeftButton:

            if self.parent().checkbox.isChecked():
                return None

            pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())

            if self.parent().drawType == 0:
                self.items.clear()
                line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())

                self.scene.addLine(line, pen)

            if self.parent().drawType == 2:
                brush = QBrush(self.parent().brushcolor)

                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addRect(rect, pen, brush)

            if self.parent().drawType == 3:
                brush = QBrush(self.parent().brushcolor)

                self.items.clear()
                rect = QRectF(self.start, self.end)
                self.scene.addEllipse(rect, pen, brush)







#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    win = choose_level()
#    app.exec_()