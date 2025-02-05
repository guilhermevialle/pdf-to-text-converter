from pyproj import Transformer


# Converte coordenadas de latitude/longitude para UTM
# latlon_array: array de coordenadas lat/lon
# target_epsg: código EPSG do sistema UTM de destino
def latlon_to_utm(latlon_array, target_epsg):
    transformer = Transformer.from_crs(
        "EPSG:4326", f"EPSG:{target_epsg}", always_xy=True
    )
    return [(*transformer.transform(lon, lat), alt) for lon, lat, alt in latlon_array]


# Converte coordenadas UTM para latitude/longitude
# utm_array: array de coordenadas UTM
# source_epsg: código EPSG do sistema UTM de origem
def utm_to_latlon(utm_array, source_epsg):
    transformer = Transformer.from_crs(
        f"EPSG:{source_epsg}", "EPSG:4326", always_xy=True
    )
    return [transformer.transform(x, y) for x, y, *_ in utm_array]


# Identifica se as coordenadas estão em UTM ou lat/lon
# Retorna "utm" se as coordenadas estiverem em UTM, "latlon" se estiverem em lat/lon
def coordinates_system_identifier(coordinates):
    if not coordinates:
        return None

    x, y, _ = coordinates[0]

    if abs(x) > 180 or abs(y) > 90:
        return "utm"
    else:
        return "latlon"
