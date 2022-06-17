import numpy as np
from email.mime import image
import cv2
from PIL import Image
import pytesseract
import contextlib
import cgi
import sys


video_port = 0
video = cv2.VideoCapture(video_port)
address = sys.argv[1]
video.open(address)

while(True):
    result, image = video.read()
    cv2.imshow("Captured Image", image)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("1.png", image)
        break

imgFile = "1.png"

im = cv2.imread(imgFile)

cv2.imshow("Original Image", im)
cv2.waitKey(10000)


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray_image = grayscale(im)

thresh, im_bw = cv2.threshold(gray_image, 145, 240, cv2.THRESH_BINARY)


def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)


no_noise = noise_removal(im_bw)


ocr_result = pytesseract.image_to_string(no_noise)
file_path = 'Text_File.txt'
with open(file_path, "w") as o:
    with contextlib.redirect_stdout(o):
        print(ocr_result)
