import cv2
import pytesseract

image_path = "images/label2.jpeg"

img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)

print("===== OCR OUTPUT =====")
print(text)
