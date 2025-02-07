from pyproj import Transformer
from utils.indetifiers.index import coordinates_system_identifier


# Converte coordenadas de latitude/longitude para UTM
# latlon_coordinates: array de coordenadas lat/lon
# target_epsg: código EPSG do sistema UTM de destino
def latlon_to_utm(latlon_coordinates, target_epsg):
    # Verifica se as coordenadas já estão em UTM
    if coordinates_system_identifier(latlon_coordinates) == "utm":
        return latlon_coordinates

    transformer = Transformer.from_crs(
        "EPSG:4326", f"EPSG:{target_epsg}", always_xy=True
    )
    utm_coordinates = []
    for coord in latlon_coordinates:
        x, y = transformer.transform(coord["lon"], coord["lat"])
        utm_coord = {"x": x, "y": y, "alt": coord["alt"], "point_id": coord["point_id"]}
        utm_coordinates.append(utm_coord)
    return utm_coordinates


# Converte coordenadas UTM para latitude/longitude
# utm_coordinates: array de coordenadas UTM
# source_epsg: código EPSG do sistema UTM de origem
def utm_to_latlon(utm_coordinates, source_epsg):
    # Verifica se as coordenadas já estão em lat/lon
    if coordinates_system_identifier(utm_coordinates) == "latlon":
        return utm_coordinates

    transformer = Transformer.from_crs(
        f"EPSG:{source_epsg}", "EPSG:4326", always_xy=True
    )
    latlon_coordinates = []
    for coord in utm_coordinates:
        lon, lat = transformer.transform(coord["x"], coord["y"])
        latlon_coord = {
            "lat": lat,
            "lon": lon,
            "alt": coord["alt"],
            "point_id": coord["point_id"],
        }
        latlon_coordinates.append(latlon_coord)
    return latlon_coordinates
