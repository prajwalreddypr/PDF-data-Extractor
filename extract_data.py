from PyPDF2 import PdfReader

import pytesseract
from PIL import Image
import cv2
import os

def extract_text_from_pdf (file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    
    #insert your PDF file here
    pdf_file = "Web Applications Patterns.pdf"
    print(extract_text_from_pdf(pdf_file)) 
    
    
    
def extract_text_with_ocr(image_path):
    #Read image
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting to grayscale
    
    text = pytesseract.image_to_string(gray)
    return text