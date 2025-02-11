from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser


def get_parser(file_type):
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


def get_epsg_info(epsg: int) -> tuple[float, str]:
    # Validação para SIRGAS 2000
    if not 31965 <= epsg <= 31984:
        raise ValueError(
            "Código EPSG fornecido não é um código UTM SIRGAS 2000 válido (deve estar entre 31965 e 31984)"
        )

    zona_utm = abs(31960 - epsg)
    meridiano_central = -183 + (zona_utm * 6)
    hemisferio = "W" if meridiano_central < 0 else "E"

    return abs(meridiano_central), hemisferio
