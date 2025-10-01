from pdf2image import convert_from_path
import os

# Task: Convert PDF pages into images (one image per page)

def pdf_to_images(pdf_path, output_folder="output_images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pages = convert_from_path(pdf_path, dpi=300)  # higher dpi = better OCR
    image_paths = []

    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        page.save(image_path, "PNG")
        image_paths.append(image_path)

    return image_paths

if __name__ == "__main__":
    pdf_path = "Complete Machine Learning Terms.pdf"  # put your PDF here
    images = pdf_to_images(pdf_path)
    print(f"Converted {len(images)} pages into images:", images)
