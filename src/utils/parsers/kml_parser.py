import xml.etree.ElementTree as ET


def kml_parser(file_path: str):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        namespaces = {"kml": "http://www.opengis.net/kml/2.2"}

        coordinates_list = []

        for coord in root.findall(".//kml:coordinates", namespaces):
            coord_text = coord.text.strip()
            for point in coord_text.split():
                lon, lat, *_ = map(float, point.split(","))
                coordinates_list.append((lon, lat))

        return coordinates_list

    except Exception as e:
        print(f"Error parsing KML file: {e}")
        return []
