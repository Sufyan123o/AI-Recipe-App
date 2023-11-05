# cv2/pillow/pytesseract ... text recognition through video
import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _, myImage = camera.read()
    cv2.imshow('Text detection', myImage)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test1.jpg', myImage)
        break
camera.release()
cv2.destroyAllWindows


def tesseract():
    path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    Imagepath = 'test1.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(myImage.open(Imagepath))
    print(text)


tesseract()
