import xml.etree.ElementTree as ET


# Função para analisar e extrair coordenadas de um arquivo KML
# file_path: caminho do arquivo KML
# Retorna uma lista de dicionários contendo as coordenadas dos vértices
# Cada dicionário contém:
# - lat: latitude do ponto
# - lon: longitude do ponto
# - alt: altitude do ponto
# - point_id: identificador único do vértice (V1, V2, etc)
def kml_parser(file_path: str):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        namespaces = {"kml": "http://www.opengis.net/kml/2.2"}
        coordinates_list = []
        vertex_count = 1

        for coord in root.findall(".//kml:coordinates", namespaces):
            coord_text = coord.text.strip()
            for point in coord_text.split():
                lon, lat, alt = map(float, point.split(","))
                coordinates_list.append(
                    {"lat": lat, "lon": lon, "alt": alt, "point_id": f"V{vertex_count}"}
                )
                vertex_count += 1
        return coordinates_list

    except Exception as e:
        print(f"Error parsing KML file: {e}")
        return []
