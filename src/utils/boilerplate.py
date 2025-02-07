from utils.math.index import calculate_area, calculate_perimeter
from utils.indetifiers.index import coordinates_system_identifier


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
    # Chama a função boilerplate e concatena com utm_header
    description_text = boilerplate(coordinates)
    full_text = utm_header + "\n" + description_text
    return full_text


def boilerplate(coordinates):
    text = "Inicia-se a descrição deste perímetro no vértice "

    # Identify the coordinate system
    coord_system = coordinates_system_identifier(coordinates)

    for i, coord in enumerate(coordinates):
        point_id = coord.get(
            "point_id", f"V{i+1}"
        )  # Default to "V{i+1}" if point_id is missing

        if i == len(coordinates) - 1:
            text += f"terminando em {point_id} "
        else:
            text += f"{point_id} "

        # Extract altitude, or use a default if not provided
        altitude = coord.get("alt", "altura não especificada")

        if coord_system == "latlon":
            text += f"{coord['lat']:.6f} {coord['lon']:.6f}"
        elif coord_system == "utm":
            easting = coord["x"]
            northing = coord["y"]
            text += f"{easting:.2f}m E {northing:.2f}m N"
        else:
            text += "Coordenadas inválidas"

        if i < len(coordinates) - 1:
            text += ", "

    return text
