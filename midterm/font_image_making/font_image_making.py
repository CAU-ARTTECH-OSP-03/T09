from PIL import Image, ImageDraw, ImageFont
import cv2
from skimage.metrics import structural_similarity as compare_ssim
import time

def make_font_image(font_name) :
    im = Image.open("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/whitewithgrid.jpg")

    if font_name.upper() == font_name.lower() :  #폰트이름이전체한글이고, 한글폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 80)
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
        draw.text(((860 - w1) / 2.0, 125), row1, font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 80),
                  fill=(224, 224, 224))
        draw.text(((860 - w2) / 2.0, 245), row2, font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 80),
                  fill=(224, 224, 224))
        draw.text(((860 - w3) / 2.0, 365), row3, font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 80),
                  fill=(224, 224, 224))
        draw.text(((860 - w4) / 2.0, 485), row4, font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".otf", 80),
                  fill=(224, 224, 224))
        im.save("fontimage_" + font_name + ".png")
    else :                                       #폰트이름이전체 영어이고, 영어폰트일경우
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80)
        row0 = font_name
        row1 = 'a  b  c  d  e  f  g'
        row2 = 'h  i  j  k  l  m  n'
        row3 = 'o  p  q  r  s  t  u'
        row4 = 'v  w  x  y  z'
        w0,h0 = draw.textsize(row0, font = myfont0)
        w1,h1 = draw.textsize(row1 , font = myfont1)
        w2, h2 = draw.textsize(row2, font=myfont1)
        w3, h3 = draw.textsize(row3, font=myfont1)
        w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860-w0)/2.0, 50), font_name, font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40), fill='black')
        draw.text(((860-w1)/2.0, 125), row1 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        draw.text(((860-w2)/2.0, 245), row2 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        draw.text(((860-w3)/2.0, 365), row3,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        draw.text(((860-w4)/2.0, 485), row4,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        im.save("fontimage_"+font_name+".png")

while (True):
    A = input('어떠한 폰트를 원하시나요? 1. bahnschrift 2. segoesc')
    if (A == "1") :
        make_font_image("bahnschrift")
        break

    elif (A =="2") :
        make_font_image("segoesc")
        break


#이미지 경로
imageA = r"C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_original.png"
imageB = r"C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_mydrawing.png"

#이미지 읽어오기
imageB_imread = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_mydrawing.png")
imageA_imread = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_original.png")

# 결과 이미지 생성
result_image = imageB_imread.copy()

#이미지 grayscale로 변경
gray_imageA = cv2.imread(imageA, cv2.IMREAD_GRAYSCALE)
gray_imageB = cv2.imread(imageB, cv2.IMREAD_GRAYSCALE)

(score, diff) = compare_ssim(gray_imageA, gray_imageB, full=True)

diff = (diff*255).astype("uint8")

#print(f"Similarity: {score:.5f}")

a = round(score,4)
print("유사도에 따른 점수입니다")
if (a > 0.9650) :
    print('5점 만점에 5점입니다')
elif (a > 0.9500) :
    print('5점 만점에 4점입니다')
elif (a > 0.9350) :
    print('5점 만점에 3점입니다')
elif (a > 0.9200) :
    print('5점 만점에 2점입니다')
elif (a > 0.9050) :
   print('5점 만점에 1점입니다')

while (True): #피드백 난도를 결정하는 부분
    char_level = input("어느 정도로 정확한 피드백을 원하나요? \n 상(매우 정교함), 중(보통), 하(형태만 확인) 중 선택해주세요.")

    if char_level =="상":
        level = 70
        break

    elif char_level =="중":
        level = 200
        break

    elif char_level == "하":
        level = 250
        break

    else:
        print("다시 입력해 주세요")

print("이미지의 빨간색은 폰트와 어긋난 부분, 검은색은 폰트와 동일한 부분입니다.")
time.sleep(1)  # 앞의 문구 표시를 위해 쉼
print("빨간색 부분에 유의하면서 다시 한번 써보세요.")
time.sleep(2)  # 앞의 문구 표시를 위해 쉼

for x in range(0, 860):  #이미지의 가로 길이
    for y in range(0,640): #이미지의 세로 길이
        if gray_imageA[y,x] > gray_imageB[y,x]: #글씨 가이드라인 제외하기
            if gray_imageA[y, x] - (gray_imageB[y, x]) > level: #사용자가 쓴 글씨가 폰트를 벗어났을 때  #level을 통해 피드백 난도 조절
                result_image[y, x] = (0, 0, 255)  #픽셀을 빨간색으로 변경

cv2.imshow("Compare", cv2.resize(result_image, (860, 640)))
cv2.waitKey(0)
