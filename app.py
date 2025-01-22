from flask import Flask, request, redirect, url_for
import os
from extract_data import extract_text_from_pdf, extract_text_with_ocr  # Import your functions

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def upload_form():
    return '''
    <!doctype html>
    <title>Upload PDF</title>
    <h1>Upload a PDF to extract text</h1>
    <form method="post" enctype="multipart/form-data" action="/upload">
        <input type="file" name="file">
        <input type="submit" value="Upload PDF">
    </form>
    <h1>Upload an Image to extract text using OCR</h1>
    <form method="post" enctype="multipart/form-data" action="/upload-image">
        <input type="file" name="file">
        <input type="submit" value="Upload Image">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(file_path)

        # Return the extracted text
        return f"<h1>Extracted Text from PDF:</h1><pre>{extracted_text}</pre>"

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Extract text from the image using OCR
        extracted_text = extract_text_with_ocr(file_path)

        # Return the extracted text
        return f"<h1>Extracted Text from Image (OCR):</h1><pre>{extracted_text}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
