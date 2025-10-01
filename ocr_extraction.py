from paddleocr import PaddleOCR

# Task: Extract text from images using PaddleOCR (pretrained OCR model)

def extract_text(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # load English OCR
    result = ocr.ocr(image_path)

    extracted_text = []
    for line in result[0]:  # loop through detected lines
        text = line[1][0]   # line[1][0] contains actual text
        extracted_text.append(text)

    return "\n".join(extracted_text)

if __name__ == "__main__":
    text = extract_text("output_images/page_1.png")
    print("OCR Extracted Text:\n", text)
