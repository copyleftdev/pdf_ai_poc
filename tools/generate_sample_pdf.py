from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path

def create_sample_pdf(pdf_path: Path):
    c = canvas.Canvas(str(pdf_path), pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "Sample PDF Document")

    # Sample email addresses
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 100, "Email addresses:")
    c.drawString(100, height - 120, "example1@example.com")
    c.drawString(100, height - 140, "example2@example.com")

    # Sample dates
    c.drawString(72, height - 180, "Dates:")
    c.drawString(100, height - 200, "01/01/2023")
    c.drawString(100, height - 220, "02/02/2023")

    # Sample phone numbers
    c.drawString(72, height - 260, "Phone numbers:")
    c.drawString(100, height - 280, "(123) 456-7890")
    c.drawString(100, height - 300, "(987) 654-3210")

    c.showPage()
    c.save()

if __name__ == "__main__":
    pdf_path = Path("data/example.pdf")
    create_sample_pdf(pdf_path)
    print(f"Sample PDF created at: {pdf_path}")
