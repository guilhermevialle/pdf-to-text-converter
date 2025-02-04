from ai import CoordinateExtractor

extractor = CoordinateExtractor()

with open("dist/text_from_img.txt", "r", encoding="utf-8") as file:
    texto = file.read()

coordenadas = extractor.extract_coordinates(texto)

with open("dist/coordinates.txt", "w", encoding="utf-8") as file:
    file.write(str(coordenadas))

print("Processo concluído. Coordenadas salvas em 'dist/coordinates.txt'.")
