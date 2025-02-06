# Função que gera um texto descritivo a partir de uma lista de coordenadas
# Args:
#     coordinates (list): Lista de dicionários contendo coordenadas no formato UTM ou LatLon
# Returns:
#     str: Texto descritivo formatado com as coordenadas
def boilerplate(coordinates):
    text = "Inicia-se em "

    for i, coord in enumerate(coordinates, 1):
        if i == len(coordinates):
            text += f"terminando em V{i} "
        else:
            text += f"V{i} "

        if "lat" in coord and "lon" in coord:
            text += f"{coord['lat']:.6f} {coord['lon']:.6f} altura 0"
        else:
            easting = coord["x"]
            northing = coord["y"]
            text += f"{easting:.2f}m E {northing:.2f}m N altura 0"

        if i < len(coordinates):
            text += ", "

    return text
