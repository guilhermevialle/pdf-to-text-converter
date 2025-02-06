from math import radians, sin, cos, sqrt, atan2


def calculate_area(coordinates: list) -> float:
    if not coordinates or len(coordinates) < 3:
        return 0.0

    # Verifica se são coordenadas UTM ou LatLon
    is_utm = "x" in coordinates[0]

    area = 0.0

    if is_utm:
        # Cálculo para coordenadas UTM
        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)
            area += coordinates[i]["x"] * coordinates[j]["y"]
            area -= coordinates[j]["x"] * coordinates[i]["y"]

        area = abs(area) / 2.0

    else:
        # Cálculo para coordenadas LatLon usando a fórmula de Gauss modificada
        # para coordenadas esféricas
        R = 6371000  # Raio médio da Terra em metros

        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)

            lat1 = radians(coordinates[i]["lat"])
            lon1 = radians(coordinates[i]["lon"])
            lat2 = radians(coordinates[j]["lat"])
            lon2 = radians(coordinates[j]["lon"])

            area += (lon2 - lon1) * (2 + sin(lat1) + sin(lat2))

        area = abs(area * R * R / 2.0)

    return round(area, 2)
