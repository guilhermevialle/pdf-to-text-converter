import re
import os
from typing import List, Tuple, Union


class CoordinateExtractor:
    def __init__(self):
        # Regex patterns for different coordinate formats
        self.utm_pattern = r"E\s*=\s*(\d+[.,]\d+)\s*m\s*[;,]\s*N\s*=\s*(\d+[.,]\d+)\s*m"
        self.azimute_pattern = r"azimute\s+(\d+)°(\d+)\'(\d+)\""

    def read_example_file(self, filename: str) -> str:
        """Read content from a text file"""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found")

    def extract_coordinates(self, text: str) -> List[dict]:
        """Extract all coordinates from the given text"""
        coordinates = []
        vertices = {}

        # Find UTM coordinates
        matches = re.finditer(self.utm_pattern, text)
        for match in matches:
            easting = float(match.group(1).replace(",", "."))
            northing = float(match.group(2).replace(",", "."))

            # Look for vertex number in surrounding text
            prev_text = text[max(0, match.start() - 50) : match.start()]
            vertex_match = re.search(r"V(\d+)\s*\(coordenadas:", prev_text)
            vertex_number = vertex_match.group(1) if vertex_match else None

            coord_data = {
                "type": "UTM",
                "vertex": f"V{vertex_number}" if vertex_number else "Unknown",
                "easting": easting,
                "northing": northing,
            }

            if vertex_number:
                vertices[f"V{vertex_number}"] = coord_data
            coordinates.append(coord_data)

        # Find azimuths
        azimuth_matches = re.finditer(self.azimute_pattern, text)
        for match in azimuth_matches:
            degrees = int(match.group(1))
            minutes = int(match.group(2))
            seconds = int(match.group(3))

            # Look for vertices in surrounding text
            prev_text = text[max(0, match.start() - 100) : match.start()]
            vertices_match = re.search(r"V(\d+)\s+e\s+V(\d+)", prev_text)
            if vertices_match:
                from_vertex = f"V{vertices_match.group(1)}"
                to_vertex = f"V{vertices_match.group(2)}"

                coordinates.append(
                    {
                        "type": "Azimuth",
                        "from": from_vertex,
                        "to": to_vertex,
                        "angle": f"{degrees}°{minutes}'{seconds}\"",
                    }
                )

        return self._format_output(coordinates)

    def _format_output(self, coordinates: List[dict]) -> str:
        """Format the coordinates into a readable string"""
        output = []

        # Group coordinates by vertex
        vertices = {}
        azimuths = []

        for coord in coordinates:
            if coord["type"] == "UTM":
                vertices[coord["vertex"]] = coord
            elif coord["type"] == "Azimuth":
                azimuths.append(coord)

        # Format vertices
        output.append("=== Vertices (UTM Coordinates) ===")
        for vertex, data in sorted(vertices.items()):
            output.append(f"{vertex}:")
            output.append(f"  E: {data['easting']:.2f}m")
            output.append(f"  N: {data['northing']:.2f}m")

        # Format azimuths
        if azimuths:
            output.append("\n=== Azimuths ===")
            for azimuth in azimuths:
                output.append(
                    f"From {azimuth['from']} to {azimuth['to']}: {azimuth['angle']}"
                )

        return "\n".join(output)


def main():
    extractor = CoordinateExtractor()
    try:
        text = extractor.read_example_file("coordinates_example.txt")
        result = extractor.extract_coordinates(text)
        print(result)
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
