import pyttsx3
import PyPDF2
import pdfplumber

pdf_name = "example.pdf"

book = open(pdf_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print(pages)

# the page you want to start reading
start_page = 0

with pdfplumber.open(pdf_name) as pdf:
    for i in range(start_page, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
