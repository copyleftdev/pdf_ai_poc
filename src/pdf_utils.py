from pathlib import Path
import PyPDF2

def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extracts text from a PDF file.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text from the PDF.
    """
    try:
        with pdf_path.open("rb") as file:
            reader = PyPDF2.PdfReader(file)
            return "".join(page.extract_text() + "\n" for page in reader.pages)
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""