from pytesseract import pytesseract
from PIL import Image

# convert an image with text to console text

def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = 'test.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text[:-1])

    with open('text.txt', 'w') as f:
        f.write(text)


tesseract()
