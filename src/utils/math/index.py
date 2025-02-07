from math import radians, sin, cos, sqrt, atan2
import math


# Calcula a área de um polígono a partir de uma lista de coordenadas
# coordinates: lista de dicionários contendo coordenadas (UTM ou LatLon)
# unit: unidade de área ('m2', 'km2', 'ha') - padrão é 'm2'
# Retorna: área calculada na unidade especificada (float)
def calculate_area(coordinates: list, unit: str = "m2") -> float:
    if not coordinates or len(coordinates) < 3:
        return 0.0

    # Check if coordinates are UTM or LatLon
    is_utm = "x" in coordinates[0]

    area = 0.0

    if is_utm:
        # Calculation for UTM coordinates
        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)
            area += coordinates[i]["x"] * coordinates[j]["y"]
            area -= coordinates[j]["x"] * coordinates[i]["y"]

        area = abs(area) / 2.0

    else:
        # Calculation for LatLon coordinates using modified Gauss formula
        R = 6371000  # Average Earth radius in meters

        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)

            lat1 = radians(coordinates[i]["lat"])
            lon1 = radians(coordinates[i]["lon"])
            lat2 = radians(coordinates[j]["lat"])
            lon2 = radians(coordinates[j]["lon"])

            area += (lon2 - lon1) * (2 + sin(lat1) + sin(lat2))

        area = abs(area * R * R / 2.0)

    # Unit conversion
    if unit.lower() == "km2":
        area /= 1_000_000  # m² to km²
    elif unit.lower() == "ha":
        area /= 10_000  # m² to hectares

    return round(area, 2)


# Calcula o perímetro de um polígono a partir de uma lista de coordenadas
# coordinates: lista de dicionários contendo coordenadas (UTM ou LatLon)
# unit: unidade de distância ('m', 'km') - padrão é 'm'
# Retorna: perímetro calculado na unidade especificada (float)
def calculate_perimeter(coordinates: list, unit: str = "m") -> float:
    if not coordinates or len(coordinates) < 2:
        return 0.0

    # Check if coordinates are UTM or LatLon
    is_utm = "x" in coordinates[0]

    perimeter = 0.0

    if is_utm:
        # Calculation for UTM coordinates using Euclidean distance
        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)
            dx = coordinates[j]["x"] - coordinates[i]["x"]
            dy = coordinates[j]["y"] - coordinates[i]["y"]
            perimeter += sqrt(dx * dx + dy * dy)

    else:
        # Calculation for LatLon coordinates using Haversine formula
        R = 6371000  # Average Earth radius in meters

        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)

            lat1 = radians(coordinates[i]["lat"])
            lon1 = radians(coordinates[i]["lon"])
            lat2 = radians(coordinates[j]["lat"])
            lon2 = radians(coordinates[j]["lon"])

            dlat = lat2 - lat1
            dlon = lon2 - lon1

            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            perimeter += R * c

    # Convert to kilometers if requested
    if unit.lower() == "km":
        perimeter /= 1000

    return round(perimeter, 2)


# Converte um ângulo decimal para graus, minutos e segundos
# Args:
#     angulo (float): Ângulo em graus decimais
# Returns:
#     str: String formatada com graus, minutos e segundos
def dec_to_gms(angulo):
    graus = int(angulo)
    minutos = int((angulo - graus) * 60)
    segundos = ((angulo - graus) * 60 - minutos) * 60
    return f"{graus}° {minutos}’ {segundos:.2f}”"


# Calcula os azimutes entre pontos consecutivos
# Args:
#     pontos (list): Lista de dicionários contendo as coordenadas dos pontos
# Returns:
#     list: Lista de dicionários com os azimutes calculados entre os pontos
def get_azimutes(coordinates):
    azimutes = []

    for i in range(len(coordinates) - 1):
        p1, p2 = coordinates[i], coordinates[i + 1]
        delta_x = p2["x"] - p1["x"]
        delta_y = p2["y"] - p1["y"]

        azimute_rad = math.atan2(delta_y, delta_x)
        azimute_degrees = math.degrees(azimute_rad)

        if azimute_degrees < 0:
            azimute_degrees += 360

        azimutes.append(
            {
                "de": p1["point_id"],
                "para": p2["point_id"],
                "azimute": dec_to_gms(azimute_degrees),
            }
        )

    return azimutes


def get_distances(coordinates):
    distances = []

    for i in range(len(coordinates) - 1):
        p1, p2 = coordinates[i], coordinates[i + 1]
        distance = math.sqrt((p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"]) ** 2)

        distances.append(
            {
                "de": p1["point_id"],
                "para": p2["point_id"],
                "distancia_m": round(distance, 3),
            }
        )

    return distances
