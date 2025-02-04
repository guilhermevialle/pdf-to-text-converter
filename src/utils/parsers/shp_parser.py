import zipfile
import shapefile
import os
from pyproj import CRS, Transformer
import pyproj


def unzip_shp(zip_path, extract_to="temp_shp"):
    try:
        os.makedirs(extract_to, exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)

        shp_file = None
        prj_file = None
        for file in os.listdir(extract_to):
            file_path = os.path.join(extract_to, file)
            if file.lower().endswith(".shp"):
                shp_file = file_path
            elif file.lower().endswith(".prj"):
                prj_file = file_path

        if not shp_file:
            print("No .shp file found in the ZIP.")
            return None, None

        return shp_file, prj_file
    except Exception as e:
        print(f"Error unzipping SHP file: {e}")
        return None, None


def get_crs_from_prj(prj_path):
    try:
        with open(prj_path, "r") as prj_file:
            prj_text = prj_file.read()
            try:
                crs = CRS.from_wkt(prj_text)
                return crs
            except pyproj.exceptions.CRSError:
                try:
                    crs = CRS.from_proj4(prj_text)  # or CRS.from_string(prj_text)
                    return crs
                except pyproj.exceptions.CRSError as e:
                    print(f"Error parsing projection from .prj: {e}")
                    return None
    except FileNotFoundError:
        return None  # Return None if file not found
    except Exception as e:
        print(f"Error reading .prj file: {e}")
        return None


def shp_parser(zip_path, extract_to="temp_shp"):
    try:
        shp_file, prj_file = unzip_shp(zip_path, extract_to)
        if not shp_file:
            return []

        source_crs = get_crs_from_prj(prj_file)

        if source_crs is None:  # .prj missing or invalid
            try:
                with shapefile.Reader(shp_file) as sf:
                    if sf.crs:  # Check if .shp itself has CRS info
                        try:
                            source_crs = CRS.from_wkt(
                                sf.crs
                            )  # or CRS.from_string(sf.crs)
                            print("Projection info read from .shp file")
                        except pyproj.exceptions.CRSError as e:
                            print(f"Error parsing CRS from .shp: {e}")
                            source_crs = None  # Set to None to trigger the next check

                    if source_crs is None:  # No CRS in .prj or .shp
                        # *** CRITICAL: MANUAL INTERVENTION REQUIRED ***
                        print(
                            "WARNING: No projection information found.  You MUST manually specify the CRS."
                        )
                        print(
                            "Use a GIS software (like QGIS) to determine the correct EPSG code or WKT."
                        )

                        # Example: Replace 2193 with the ACTUAL EPSG of your shapefile
                        # source_crs = CRS.from_epsg(2193)
                        # OR, if you have the WKT:
                        # source_crs = CRS.from_wkt("YOUR_WKT_STRING_HERE")

                        # If you don't know the CRS, you CANNOT reliably convert!
                        if (
                            "source_crs" not in locals()
                        ):  # to avoid error if source_crs is not defined
                            return []  # Or handle it differently (e.g., return None)

            except shapefile.ShapefileException as e:  # Catch Shapefile exceptions
                print(f"Error opening or reading shapefile: {e}")
                return []
            except Exception as e:
                print(f"Error reading .shp: {e}")
                return []

        # *** Corrected: Added a try...except block here ***
        try:  # The code that might raise an exception
            transformer = Transformer.from_crs(source_crs, "EPSG:4326", always_xy=True)
            coordinates_list = []

            with shapefile.Reader(shp_file) as sf:
                for shape in sf.shapes():
                    transformed_coords = [
                        transformer.transform(x, y) for x, y in shape.points
                    ]
                    coordinates_list.append(transformed_coords)

            return coordinates_list
        except Exception as e:
            print(f"Error during coordinate transformation: {e}")
            return []  # Or handle the error as needed

    except Exception as e:  # This is the outer try block's except clause
        print(f"Error parsing SHP file: {e}")
        return []
