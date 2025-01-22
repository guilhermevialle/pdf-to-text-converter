import os
from pdf_to_img import convert_pdf_to_image
from img_to_text import extract_text_from_image

pdf_path = "../examples/Matrícula Inteiro Teor nº 1173 - Mario Lúcio.pdf"
output_folder = "../dist"
output_text_file = os.path.join(output_folder, "text_from_img.txt")
output_image_path = os.path.join(output_folder, "img_from_pdf.jpg")
poppler_path = r"C:\ProgramData\chocolatey\lib\poppler\tools\Library\bin"

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

convert_pdf_to_image(pdf_path, output_image_path, poppler_path)
text = extract_text_from_image(output_image_path, output_text_file)

print("Texto extraído:\n", text)
