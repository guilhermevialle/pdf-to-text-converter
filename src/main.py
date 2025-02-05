from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser
from constants.reference import epgs
from utils.transformers.index import latlon_to_utm, utm_to_latlon

files = {
    "KML": "assets/shapes/quadra- nova venecia.kml",
    "SHP": "assets/shapes/quadra - nova venecial.zip",
    "DXF": "assets/shapes/quadra - nova venecia.dxf",
}

coordinates = {
    "KML": latlon_to_utm(kml_parser(files["KML"], epgs), epgs),
    "SHP": shp_parser(files["SHP"], epgs),
    "DXF": dxf_parser(files["DXF"], epgs),
}


def print_coordinates(coordinates):
    for format_type, coords in coordinates.items():
        print(f"{format_type} Coordinates:")
        print(coords)
        print("\n" + "-" * 28 + "\n")


print_coordinates(coordinates)
