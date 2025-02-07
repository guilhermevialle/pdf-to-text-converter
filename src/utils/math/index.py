from math import radians, sin, cos, sqrt, atan2
import math


# Calcula a área de um polígono a partir de uma lista de coordenadas
# coordinates: lista de dicionários contendo coordenadas (UTM ou LatLon)
# Retorna: área em metros quadrados (float)
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


# Calcula o perímetro de um polígono a partir de uma lista de coordenadas
# coordinates: lista de dicionários contendo coordenadas (UTM ou LatLon)
# Retorna: perímetro em metros (float)
def calculate_perimeter(coordinates: list) -> float:
    if not coordinates or len(coordinates) < 2:
        return 0.0

    # Verifica se são coordenadas UTM ou LatLon
    is_utm = "x" in coordinates[0]

    perimeter = 0.0

    if is_utm:
        # Cálculo para coordenadas UTM usando distância euclidiana
        for i in range(len(coordinates)):
            j = (i + 1) % len(coordinates)
            dx = coordinates[j]["x"] - coordinates[i]["x"]
            dy = coordinates[j]["y"] - coordinates[i]["y"]
            perimeter += sqrt(dx * dx + dy * dy)

    else:
        # Cálculo para coordenadas LatLon usando fórmula de Haversine
        R = 6371000  # Raio médio da Terra em metros

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

    return round(perimeter, 2)


# Converte um ângulo decimal para graus, minutos e segundos
# Args:
#     angulo (float): Ângulo em graus decimais
# Returns:
#     str: String formatada com graus, minutos e segundos
def decimal_para_gms(angulo):
    graus = int(angulo)
    minutos = int((angulo - graus) * 60)
    segundos = ((angulo - graus) * 60 - minutos) * 60
    return f"{graus}° {minutos}’ {segundos:.2f}”"


# Calcula os azimutes entre pontos consecutivos
# Args:
#     pontos (list): Lista de dicionários contendo as coordenadas dos pontos
# Returns:
#     list: Lista de dicionários com os azimutes calculados entre os pontos
def calcular_azimutes(pontos):
    azimutes = []

    for i in range(len(pontos) - 1):
        p1, p2 = pontos[i], pontos[i + 1]
        delta_x = p2["x"] - p1["x"]
        delta_y = p2["y"] - p1["y"]

        azimute_rad = math.atan2(delta_y, delta_x)
        azimute_graus = math.degrees(azimute_rad)

        if azimute_graus < 0:
            azimute_graus += 360

        azimutes.append(
            {
                "de": p1["point_id"],
                "para": p2["point_id"],
                "azimute": decimal_para_gms(azimute_graus),
            }
        )

    return azimutes


def calcular_distancias(pontos):
    distancias = []

    for i in range(len(pontos) - 1):
        p1, p2 = pontos[i], pontos[i + 1]
        distancia = math.sqrt((p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"]) ** 2)

        distancias.append(
            {
                "de": p1["point_id"],
                "para": p2["point_id"],
                "distancia_m": round(distancia, 3),
            }
        )

    return distancias
