from pyproj import Transformer
from utils.indetifiers.index import coordinates_system_identifier


# Converte coordenadas de latitude/longitude para UTM
# latlon_array: array de coordenadas lat/lon
# target_epsg: código EPSG do sistema UTM de destino
def latlon_to_utm(latlon_array, target_epsg):
    # Verifica se as coordenadas já estão em UTM
    if coordinates_system_identifier(latlon_array) == "utm":
        return latlon_array

    transformer = Transformer.from_crs(
        "EPSG:4326", f"EPSG:{target_epsg}", always_xy=True
    )
    utm_array = []
    for coord in latlon_array:
        x, y = transformer.transform(coord["lon"], coord["lat"])
        utm_coord = {"x": x, "y": y, "alt": coord["alt"], "point_id": coord["point_id"]}
        utm_array.append(utm_coord)
    return utm_array


# Converte coordenadas UTM para latitude/longitude
# utm_array: array de coordenadas UTM
# source_epsg: código EPSG do sistema UTM de origem
def utm_to_latlon(utm_array, source_epsg):
    # Verifica se as coordenadas já estão em lat/lon
    if coordinates_system_identifier(utm_array) == "latlon":
        return utm_array

    transformer = Transformer.from_crs(
        f"EPSG:{source_epsg}", "EPSG:4326", always_xy=True
    )
    latlon_array = []
    for coord in utm_array:
        lon, lat = transformer.transform(coord["x"], coord["y"])
        latlon_coord = {
            "lat": lat,
            "lon": lon,
            "alt": coord["alt"],
            "point_id": coord["point_id"],
        }
        latlon_array.append(latlon_coord)
    return latlon_array
