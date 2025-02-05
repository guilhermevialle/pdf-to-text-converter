from pyproj import Transformer


def latlon_to_utm(latlon_array, target_epsg):
    transformer = Transformer.from_crs(
        "EPSG:4326", f"EPSG:{target_epsg}", always_xy=True
    )
    return [(*transformer.transform(lon, lat), alt) for lon, lat, alt in latlon_array]


def utm_to_latlon(utm_array, source_epsg):
    transformer = Transformer.from_crs(
        f"EPSG:{source_epsg}", "EPSG:4326", always_xy=True
    )
    return [transformer.transform(x, y) for x, y, *_ in utm_array]
