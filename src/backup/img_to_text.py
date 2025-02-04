import cv2
import pytesseract


def extract_text_from_image(image_path, output_file):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)
    custom_config = r"--oem 3 --psm 6"
    text = pytesseract.image_to_string(denoised, lang="por+eng", config=custom_config)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Texto extraído salvo em: {output_file}")
