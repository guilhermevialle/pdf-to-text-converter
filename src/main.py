from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser

kml = "assets/shapes/quadra- nova venecia.kml"
shp = "assets/shapes/quadra - nova venecia.zip"


kml_coordinates = kml_parser(kml)
shp_coordinates = shp_parser(shp)

print(kml_coordinates, "\n", shp_coordinates)
