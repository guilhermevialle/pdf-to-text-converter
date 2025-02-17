from utils.math.index import calculate_area, calculate_perimeter
from utils.indetifiers.index import coordinates_system_identifier
from datetime import datetime
from utils.helpers.index import get_epsg_info
from constants.reference import epsg
import re
from utils.math.index import get_azimutes, get_distances


def text_info():
    date = datetime.now().strftime("%d/%m/%Y")
    return date


def sigef_memorial_boilerplate(
    coordinates,
    epsg: int,
    include_height: bool,
    vertex_id: str = None,
):
    area = calculate_area(coordinates, "ha")
    perimeter = calculate_perimeter(coordinates, "m")
    meridiano, hemisferio = get_epsg_info(epsg)

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
Todas as coordenadas aqui descritas estão georreferenciadas ao Sistema Geodésico Brasileiro e encontram-se representadas no Sistema UTM, referenciadas ao Meridiano Central nº {meridiano} {hemisferio}Gr, tendo como Datum o SIRGAS2000. Todos os azimutes e distâncias, área e perímetro foram calculados no plano de projeção UTM.
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

    description_text = boilerplate(coordinates, epsg, include_height, vertex_id)
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


def boilerplate(
    coordinates,
    epsg: int,
    include_height: bool,
    vertex_id: str = None,
):
    text = "Inicia-se a descrição deste perímetro no vértice "
    meridiano, hemisferio = get_epsg_info(epsg)
    first_vertex_text = f", georreferenciado no Sistema Geodésico Brasileiro, DATUM - SIRGAS2000, MC-{meridiano}º{hemisferio} "

    # Obter azimutes e distâncias
    azimutes = get_azimutes(coordinates)
    distances = get_distances(coordinates)

    # Identifica o sistema de coordenadas
    coord_system = coordinates_system_identifier(coordinates)

    for i, coord in enumerate(coordinates):
        if vertex_id:
            if re.search(r"\d$", vertex_id):
                point_id = f"{vertex_id}-{i+1}"
            else:
                point_id = f"{vertex_id}{i+1}"
        else:
            point_id = coord.get("point_id", f"V{i+1}")

        # Construindo o texto para as coordenadas
        coord_text = ""
        if coord_system == "utm":
            coord_text = f"de coordenadas N {coord['y']:.2f}m e E {coord['x']:.2f}m"
            if include_height and "alt" in coord:
                coord_text += f" de altitude {coord['alt']:.2f}m"

        # Primeiro vértice
        if i == 0:
            text += f"{point_id}{first_vertex_text}{coord_text}"
        # Vértices intermediários e final
        else:
            prev_azimute = azimutes[i - 1]["azimute"]
            prev_distance = distances[i - 1]["distancia_m"]

            text += f"; deste segue, com azimute de {prev_azimute} por uma distância de {prev_distance:.2f}m até o vértice {point_id}, {coord_text}"

    text += "."
    return text
