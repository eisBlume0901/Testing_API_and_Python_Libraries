import os
from dotenv import load_dotenv
import PyPDF2
load_dotenv()

def get_pdf_page_count(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return len(reader.pages)
    except Exception as e:
        raise RuntimeError(f"Failed to extract page count from PDF: {e}")

# Example usage
file_path = os.getenv("TEST_FILE_PATH_PDF")
try:
    page_count = get_pdf_page_count(file_path)
    print(f"Number of pages: {page_count}")
except Exception as e:
    print(e)

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {e}")

# Example usage
load_dotenv()

file_path = os.getenv("TEST_FILE_PATH_PDF")
try:
    text = extract_text_from_pdf(file_path)
    print(text)
except Exception as e:
    print(e)