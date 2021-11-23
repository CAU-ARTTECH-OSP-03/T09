import cv2
from skimage.metrics import structural_similarity as compare_ssim


imageA0 = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_original.png")
imageB0 = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_mydrawing.png")
imageA = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/bahnschrift_original.png")
imageB = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/bahnschrift_,mydrawing.png")
imageC = imageA.copy()
imageF = imageA0.copy()

tempDiff = cv2.subtract(imageA, imageB)


grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
#cv2.imshow("grayA", cv2.resize(grayA, (960, 540)))

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
#print(f"Similarity: {score:.5f}")

assert score, "다른 점 찾을 수 없음"

thresh = cv2.threshold(diff, 0, 255,
                       cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# 차이점 빨간색으로 칠하기
tempDiff[thresh == 255] = [0, 0, 255]
imageC[thresh == 255] = [0, 0, 255]

# 다른 점 diff3.png로 저장
cv2.imwrite("D:\DEV\Code\Python\img\diff3.png", imageC)


# 결과 출력
cv2.imshow("Original", cv2.resize(imageA, (960, 540)))
cv2.imshow("Compare", cv2.resize(imageB, (960, 540)))
cv2.imshow("Difference", cv2.resize(imageC, (960, 540)))
#cv2.imshow("Gray", cv2.resize(diff, (960, 540)))
#cv2.imshow("Gray2", cv2.resize(tempDiff, (960, 540)))

# 아무 키나 눌러서 종료하기
cv2.waitKey(0)

