# Identifica se as coordenadas estão em UTM ou lat/lon
# coordinates: array de coordenadas em UTM ou lat/lon
# Retorna "utm" se as coordenadas estiverem em UTM, "latlon" se estiverem em lat/lon
def coordinates_system_identifier(coordinates):
    if not coordinates:
        return None

    x, y, _ = coordinates[0]

    if abs(x) > 180 or abs(y) > 90:
        return "utm"
    else:
        return "latlon"


# Identifica o tipo de arquivo com base em sua extensão
# file_path: caminho do arquivo
# Retorna "kml" para arquivos KML, "shp" para arquivos SHP/ZIP, "dxf" para arquivos DXF, ou None se não reconhecido
def file_identifier(file_path):
    extension = file_path.lower().split(".")[-1]
    if extension == "kml":
        return "kml"
    elif extension in ["shp", "zip"]:
        return "shp"
    elif extension == "dxf":
        return "dxf"
    return None
