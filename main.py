import cv2
import os
import pytesseract
from pathlib import Path


dir_path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir_path, "test2.png")

img = cv2.imread(filename)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))

cv2.imshow('Result',img)
cv2.waitkey(0)

