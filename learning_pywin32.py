import pythoncom
import os
from dotenv import load_dotenv
from win32com.client import DispatchEx

def get_document_statistics(file_path):
    try:
        pythoncom.CoInitialize()
    except Exception as e:
        raise RuntimeError(f"Failed to initialize COM library: {e}")

    try:
        word = DispatchEx("Word.Application")
    except Exception as e:
        raise RuntimeError(f"Failed to create COM object: {e}")

    try:
        doc = word.Documents.Open(file_path)
        stats = {
            'page_count': doc.ComputeStatistics(2),  # 2 corresponds to the number of pages
            'word_count': doc.ComputeStatistics(0),  # 0 corresponds to the number of words
            'character_count': doc.ComputeStatistics(1)  # 1 corresponds to the number of characters
        }
        doc.Close()
        word.Quit()
        return stats
    except Exception as e:
        word.Quit()
        raise RuntimeError(f"Failed to process the document: {e}")

# Example usage
load_dotenv()
file_path = os.getenv("TEST_FILE_PATH_DOCX")

try:
    stats = get_document_statistics(file_path)
    print(stats)
except Exception as e:
    print(e)