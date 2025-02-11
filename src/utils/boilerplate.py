from utils.math.index import calculate_area, calculate_perimeter
from utils.indetifiers.index import coordinates_system_identifier
import re
from datetime import datetime
from utils.helpers.index import get_epsg_info
from constants.reference import epsg


def text_info():
    date = datetime.now().strftime("%d/%m/%Y")
    return date


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

    text_ends = f"""
Todas as coordenadas aqui descritas estão georreferenciadas ao Sistema Geodésico Brasileiro e encontram-se representadas no Sistema UTM, referenciadas ao Meridiano Central nº 45 WGr, tendo como Datum o SIRGAS2000. Todos os azimutes e distâncias, área e perímetro foram calculados no plano de projeção UTM.
"""

    date_text = f"""
                                         Cidade, {text_info()}
"""

    footer_text = f"""
_______________________________________
Proprietário:
CNPJ nº ou CPF nº:

_______________________________________
Responsável Técnico:
Formação:
Código Credenciamento ASR -
CREA:
"""

    # Chama a função boilerplate e concatena com utm_header

    description_text = boilerplate(coordinates, vertex_id)
    full_text = (
        utm_header
        + "\n"
        + description_text
        + "\n"
        + text_ends
        + "\n"
        + date_text
        + "\n"
        + footer_text
    )
    return full_text


def boilerplate(coordinates, vertex_id: str = None):
    text = "Inicia-se a descrição deste perímetro no vértice "
    mc = None
    hemisphere = None
    meridiano, hemisferio = get_epsg_info(epsg)
    first_vertex_text = f", georreferenciado no Sistema Geodésico Brasileiro, DATUM - SIRGAS2000, MC-{meridiano}º{hemisferio} "

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

        if i == 0:
            text += f"{point_id}{first_vertex_text}"
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
