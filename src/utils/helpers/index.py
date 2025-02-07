from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser


def get_parser(file_type):

    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)
