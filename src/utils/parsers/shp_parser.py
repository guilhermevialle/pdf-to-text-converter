import zipfile
import shapefile
import os
from pyproj import Transformer


def shp_parser(zip_path: str, extract_to: str = "temp_shp", source_epsg: int = 31984):
    try:
        os.makedirs(extract_to, exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)

        shp_file = None
        for file in os.listdir(extract_to):
            if file.lower().endswith(".shp"):
                shp_file = os.path.join(extract_to, file)
                break

        if not shp_file:
            print("No .shp file found in the ZIP.")
            return []

        sf = shapefile.Reader(shp_file)
        coordinates_list = []
        transformer = Transformer.from_crs(
            f"EPSG:{source_epsg}", "EPSG:4326", always_xy=True
        )

        for shape in sf.shapes():
            for x, y in shape.points:
                transformed_coord = transformer.transform(x, y)
                coordinates_list.append(transformed_coord)

        return coordinates_list

    except Exception as e:
        print(f"Error parsing SHP file: {e}")
        return []
