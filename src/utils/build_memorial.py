from utils.math.index import calculate_area, calculate_perimeter
from utils.indetifiers.index import coordinates_system_identifier
from utils.helpers.index import get_epsg_info, get_date
from constants.reference import epsg
from utils.math.index import get_azimutes, get_distances
import re


def build_sigef_memorial(
    coordinates,
    epsg: int,
    include_altitude: bool,
    vertex_id: str = None,
):
    area = calculate_area(coordinates, "ha")
    perimeter = calculate_perimeter(coordinates, "m")

    utm_header = build_sigef_header(area, perimeter)
    description = build_coordinates_description(
        coordinates, epsg, include_altitude, vertex_id
    )
    footer = build_sigef_footer(epsg)
    date_section = build_date_section()
    signature_section = build_signature_section()

    full_document_text = (
        utm_header
        + "\n"
        + description
        + "\n"
        + footer
        + "\n"
        + date_section
        + "\n"
        + signature_section
    )
    return full_document_text


def build_sigef_header(area, perimeter):
    return f"""
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


def build_sigef_footer(epsg):
    meridiano, hemisferio = get_epsg_info(epsg)
    return f"""
Todas as coordenadas aqui descritas estão georreferenciadas ao Sistema Geodésico Brasileiro e encontram-se representadas no Sistema UTM, referenciadas ao Meridiano Central nº {meridiano} {hemisferio}Gr, tendo como Datum o SIRGAS2000. Todos os azimutes e distâncias, área e perímetro foram calculados no plano de projeção UTM.
"""


def build_date_section():
    return f"""
                                         Cidade, {get_date()}
"""


def build_signature_section():
    return f"""
_______________________________________
Proprietário:
CNPJ nº ou CPF nº:

_______________________________________
Responsável Técnico:
Formação:
Código Credenciamento ASR -
CREA:
"""


def build_coordinates_description(
    coordinates,
    epsg: int,
    include_altitude: bool,
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

    text += build_vertex_descriptions(
        coordinates,
        coord_system,
        include_altitude,
        vertex_id,
        first_vertex_text,
        azimutes,
        distances,
    )

    text += "."
    return text


def build_vertex_descriptions(
    coordinates,
    coord_system,
    include_altitude,
    vertex_id,
    first_vertex_text,
    azimutes,
    distances,
):
    text = ""

    for i, coord in enumerate(coordinates):
        point_id = generate_point_id(vertex_id, i, coord)
        coord_text = format_coordinate_text(coord, coord_system, include_altitude)

        # Primeiro vértice
        if i == 0:
            text += f"{point_id}{first_vertex_text}{coord_text}"
        # Vértices intermediários e final
        else:
            prev_azimute = azimutes[i - 1]["azimute"]
            prev_distance = distances[i - 1]["distancia_m"]

            text += f"; deste segue, com azimute de {prev_azimute} por uma distância de {prev_distance:.2f}m até o vértice {point_id}, {coord_text}"

    return text


def generate_point_id(vertex_id, index, coord):
    if vertex_id:
        if re.search(r"\d$", vertex_id):
            point_id = f"{vertex_id}-{index+1}"
        else:
            point_id = f"{vertex_id}{index+1}"
    else:
        point_id = coord.get("point_id", f"V{index+1}")

    return point_id


def format_coordinate_text(coord, coord_system, include_altitude):
    if coord_system == "utm":
        coord_text = f"de coordenadas E {coord['y']:.2f}m e N {coord['x']:.2f}m"
        if include_altitude and "alt" in coord:
            coord_text += f" de altitude {coord['alt']:.2f}m"
    else:
        # Aqui poderia ter outros formatos de coordenadas
        coord_text = ""

    return coord_text
