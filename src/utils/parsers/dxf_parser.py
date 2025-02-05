import ezdxf
from pyproj import Transformer


def dxf_parser(file_path: str, source_epsg: int = 31984):
    try:
        doc = ezdxf.readfile(file_path)
        coordinates_list = []
        transformer = Transformer.from_crs(
            f"EPSG:{source_epsg}", "EPSG:4326", always_xy=True
        )

        for entity in doc.modelspace().query("LINE CIRCLE LWPOLYLINE POLYLINE"):
            if entity.dxftype() == "LINE":
                start_lon, start_lat = transformer.transform(
                    entity.dxf.start.x, entity.dxf.start.y
                )
                end_lon, end_lat = transformer.transform(
                    entity.dxf.end.x, entity.dxf.end.y
                )
                coordinates_list.append((start_lon, start_lat))
                coordinates_list.append((end_lon, end_lat))
            elif entity.dxftype() == "CIRCLE":
                center_lon, center_lat = transformer.transform(
                    entity.dxf.center.x, entity.dxf.center.y
                )
                coordinates_list.append((center_lon, center_lat))
            elif entity.dxftype() == "LWPOLYLINE" or entity.dxftype() == "POLYLINE":
                for vertex in entity.vertices():
                    lon, lat = transformer.transform(vertex[0], vertex[1])
                    coordinates_list.append((lon, lat))

        return coordinates_list

    except Exception as e:
        print(f"Error parsing DXF file: {e}")
        return []
