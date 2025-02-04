from pdf2image import convert_from_path
from PIL import Image


def convert_pdf_to_image(pdf_path, output_image_path, poppler_path):
    pages = convert_from_path(pdf_path, poppler_path=poppler_path)
    width, height = pages[0].size
    total_height = height * len(pages)
    final_image = Image.new("RGB", (width, total_height))
    y_offset = 0
    for page in pages:
        final_image.paste(page, (0, y_offset))
        y_offset += height
    final_image.save(output_image_path)
    print("PDF convertido para uma única imagem com sucesso!")
