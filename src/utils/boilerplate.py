from utils.math.index import calculate_area, calculate_perimeter
from utils.indetifiers.index import coordinates_system_identifier
import re


def sigef_memorial_boilerplate(coordinates, vertex_id: str = None):
    area = calculate_area(coordinates, "ha")
    perimeter = calculate_perimeter(coordinates, "m")

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
    description_text = boilerplate(coordinates, vertex_id)
    full_text = utm_header + "\n" + description_text
    return full_text


def boilerplate(coordinates, vertex_id: str = None):
    text = "Inicia-se a descrição deste perímetro no vértice "

    # Identifica o sistema de coordenadas
    coord_system = coordinates_system_identifier(coordinates)

    for i, coord in enumerate(coordinates):
        if vertex_id:
            # Check if last character is a number
            if re.search(r"\d$", vertex_id):
                point_id = f"{vertex_id}-{i+1}"  # Add "-" before the counter
            else:
                point_id = f"{vertex_id}{i+1}"  # Append counter directly
        else:
            point_id = coord.get("point_id", f"V{i+1}")  # Default fallback

        if i == len(coordinates) - 1:
            text += f"terminando em {point_id} "
        else:
            text += f"{point_id} "

        # Extrai altitude, ou usa um padrão se não fornecida
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
