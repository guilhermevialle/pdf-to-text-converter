from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser
from constants.reference import epgs
from utils.transformers.index import coordinates_system_identifier

files = {
    "KML": "assets/shapes/quadra- nova venecia.kml",
    "SHP": "assets/shapes/quadra - nova venecial.zip",
    "DXF": "assets/shapes/quadra - nova venecia.dxf",
}

coordinates = {
    "KML": kml_parser(files["KML"]),
    "SHP": shp_parser(files["SHP"]),
    "DXF": dxf_parser(files["DXF"]),
}


def print_coordinates(coordinates):
    for format_type, coords in coordinates.items():
        print(f"{format_type} Coordinates:")
        print(coords)
        print("\n" + "-" * 28 + "\n")


print_coordinates(coordinates)
