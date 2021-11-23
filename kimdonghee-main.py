import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

class compareImg :
    def __init__(self) :
        pass
    def readImg(self, filepath) :
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        # cv2.namedWindow("root", cv2.WINDOW_NORMAL) # window 생성 #
        # cv2.imshow("root", img) # window에 이미지 띄우기 #
        # cv2.waitKey(5000) # 5초 기다림. 아무키나 입력되면 대기 종료
        # cv2.destroyAllWindows() # window 제거
        return img

    def diffImg(self, img1, img2) :
        # Initiate SIFT detector
        orb = cv2.ORB_create()
        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1,des2)

        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)

        # BFMatcher with default params
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        # Apply ratio test
        good = []

        for m,n in matches:
            if m.distance < ratio * n.distance:
                good.append([m])

        # Draw first 10 matches.
        knn_image = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        plt.imshow(knn_image)
        plt.show()

    def run(self) :
        # 이미지 파일 경로 설정 #자기 컴퓨터에 이미지 경로를 넣어야 함
        #주의!! 경로에 한글 있으면 오류뜸!!
        filepath1 = r"C:\Users\user\OPimage\bahnschrift_original.png"
        filepath2 = r"C:\Users\user\OPimage\bahnschrift_,mydrawing.png"

        # 이미지 객체 가져옴
        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)

        # 2개의 이미지 비교
        self.diffImg(img1, img2)

if __name__ == '__main__':
    while(True):

        answer = input("더 자세한 피드백을 원합니까?(Y/N)")

        if answer == "N" or answer == "n": #사용자가 피드백을 원하지 않을 때
            print("수고하셨습니다!")
            break

        elif answer == 'Y' or answer == "y": #사용자가 피드백을 원할 때
            while(True):
                char_ratio = input("어느 정도로 정확한 피드백을 원하나요? \n 상(매우 정교함), 중(보통), 하(형태만 확인) 중 선택해주세요.")
                print("매칭된 포인트들은 유사도가 높은 부분입니다.")
                time.sleep(2) #앞의 문구 표시를 위해 쉼

                #ratio값 지정
                if char_ratio == '상':
                    ratio = 0.65
                    cImg = compareImg()
                    cImg.run()
                    break

                elif char_ratio == '중':
                    ratio = 0.75
                    cImg = compareImg()
                    cImg.run()
                    break

                elif char_ratio == '하':
                    ratio = 0.85
                    cImg = compareImg()
                    cImg.run()
                    break

                else:
                    print("다시 입력해 주세요")

        else:
            print("다시 입력해주세요.")

