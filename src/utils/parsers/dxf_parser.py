import ezdxf


def dxf_parser(file_path: str, source_epsg: int = 31984):
    try:
        doc = ezdxf.readfile(file_path)
        coordinates_list = []

        for entity in doc.modelspace().query("LINE CIRCLE LWPOLYLINE POLYLINE"):
            if entity.dxftype() == "LINE":
                start_z = getattr(entity.dxf.start, "z", 0)
                end_z = getattr(entity.dxf.end, "z", 0)
                coordinates_list.append(
                    (
                        float(entity.dxf.start.x),
                        float(entity.dxf.start.y),
                        float(start_z),
                    )
                )
                coordinates_list.append(
                    (float(entity.dxf.end.x), float(entity.dxf.end.y), float(end_z))
                )
            elif entity.dxftype() == "CIRCLE":
                center_z = getattr(entity.dxf.center, "z", 0)
                coordinates_list.append(
                    (
                        float(entity.dxf.center.x),
                        float(entity.dxf.center.y),
                        float(center_z),
                    )
                )
            elif entity.dxftype() == "LWPOLYLINE" or entity.dxftype() == "POLYLINE":
                for vertex in entity.vertices():
                    z = vertex[2] if len(vertex) > 2 else 0
                    coordinates_list.append(
                        (float(vertex[0]), float(vertex[1]), float(z))
                    )

        # Convert numpy float64 values to regular floats and round to 3 decimal places
        coordinates_list = [
            (round(x, 3), round(y, 3), round(z, 3)) for x, y, z in coordinates_list
        ]
        return coordinates_list

    except Exception as e:
        print(f"Error parsing DXF file: {e}")
        return []
