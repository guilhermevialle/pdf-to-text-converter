from utils.math.index import calculate_area, calculate_perimeter


# Função que gera um texto descritivo a partir de uma lista de coordenadas
# Args:
#     coordinates (list): Lista de dicionários contendo coordenadas no formato UTM ou LatLon
# Returns:
#     str: Texto descritivo formatado com as coordenadas


def sigef_memorial_boilerplate(coordinates):
    area = calculate_area(coordinates)
    perimeter = calculate_perimeter(coordinates)

    utm_header = f"""
Imóvel:
Matrícula do Imóvel:
Cartório (CNS):
Município:
Código SNCR:
Proprietário:
CNPJ nº:

Responsável Técnico:
Formação:
Código Credenciamento ASR:
CREA:

Área: {area}ha
Perímetro: {perimeter}m

Sistema Geodésico de Referência: SIRGAS2000
Azimutes: Azimutes Geodésicos

                          IMÓVEL DESCRIÇÃO
"""

    text = "Inicia-se a descrição deste perímetro no vértice "


def boilerplate(coordinates):
    for i, coord in enumerate(coordinates, 1):
        if i == len(coordinates):
            text += f"terminando em V{i} "
        else:
            text += f"V{i} "

        if "lat" in coord and "lon" in coord:
            text += f"{coord['lat']:.6f} {coord['lon']:.6f} altura 0"
        else:
            easting = coord["x"]
            northing = coord["y"]
            text += f"{easting:.2f}m E {northing:.2f}m N altura 0"

        if i < len(coordinates):
            text += ", "

    return text
