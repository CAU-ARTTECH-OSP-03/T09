import cv2
from skimage.metrics import structural_similarity as compare_ssim


imageA = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_original.png")
imageB = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/segoesc_mydrawing.png")
imageD = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/bahnschrift_original.png")
imageE = cv2.imread("C:/Users/TOP/Desktop/opensource/T09/midterm/font_image_making/fontimage/bahnschrift_,mydrawing.png")
imageC = imageA.copy()
imageF = imageD.copy()
print(imageD.shape)
print(imageE.shape)