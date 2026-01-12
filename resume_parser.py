
import PyPDF2

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file object.
    """
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text.strip()

import PyPDF2

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# from pypdf import PdfReader

# def extract_text_from_pdf(pdf_file):
#     """
#     Extracts text from a PDF file object.
#     """
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ""

#     for page in reader.pages:
#         page_text = page.extract_text()
#         if page_text:
#             text += page_text + " "

#     return text.strip()

