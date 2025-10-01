from pdf_to_images import pdf_to_images
from ocr_extraction import extract_text
from text_cleanup import clean_text
from docx import Document
from docx.shared import Pt
import os
from datetime import datetime

# Path to your PDF file
pdf_path = r"Complete Machine Learning Terms.pdf"

def process_pdf(pdf_path):
    # 1. Convert PDF to images
    images = pdf_to_images(pdf_path)

    # 2. OCR each page
    text = ""
    for i, img in enumerate(images):
        page_text = extract_text(img)
        cleaned_text = clean_text(page_text)
        text += f"\n\n--- Page {i+1} ---\n{cleaned_text}"

    return text

def is_heading(line: str) -> bool:
    """
    Detects if a line is a heading.
    - Ends with ":" OR
    - Mostly uppercase
    """
    if line.endswith(":"):
        return True

    letters = [c for c in line if c.isalpha()]
    if not letters:
        return False

    uppercase_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
    return uppercase_ratio >= 0.8

def save_as_docx(text: str, filename: str = "cleaned_output.docx"):
    doc = Document()

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue

        p = doc.add_paragraph()
        run = p.add_run(line)

        # Set font for everything
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)

        # Make headings bold
        if is_heading(line):
            run.bold = True

    # Try saving, handle locked file
    try:
        doc.save(filename)
    except PermissionError:
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
        print(f"[!] File is open, saving as {new_filename}")
        doc.save(new_filename)

if __name__ == "__main__":
    final_text = process_pdf(pdf_path)
    save_as_docx(final_text)
