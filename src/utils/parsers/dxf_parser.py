import ezdxf


# Função para analisar e extrair coordenadas de um arquivo DXF
# file_path: caminho do arquivo DXF
# Retorna uma lista de dicionários contendo as coordenadas dos vértices
# Cada dicionário contém:
# - lat/lon ou x/y: coordenadas do ponto dependendo do sistema de coordenadas
# - alt: altitude do ponto
# - point_id: identificador único do vértice (V1, V2, etc)
def dxf_parser(file_path: str):
    try:
        doc = ezdxf.readfile(file_path)
        coordinates_list = []
        vertex_count = 1

        # Obtém o sistema de coordenadas do cabeçalho DXF
        coordinates_system = doc.header.get("$INSUNITS", None)
        is_latlon = coordinates_system in [1, 2]  # 1=Científico, 2=Graus decimais

        for entity in doc.modelspace().query("LINE CIRCLE LWPOLYLINE POLYLINE"):
            if entity.dxftype() == "LINE":
                start_z = getattr(entity.dxf.start, "z", 0)
                end_z = getattr(entity.dxf.end, "z", 0)

                if is_latlon:
                    coordinates_list.append(
                        {
                            "lat": float(entity.dxf.start.y),
                            "lon": float(entity.dxf.start.x),
                            "alt": float(start_z),
                            "point_id": f"V{vertex_count}",
                        }
                    )
                    vertex_count += 1
                    coordinates_list.append(
                        {
                            "lat": float(entity.dxf.end.y),
                            "lon": float(entity.dxf.end.x),
                            "alt": float(end_z),
                            "point_id": f"V{vertex_count}",
                        }
                    )
                    vertex_count += 1
                else:
                    coordinates_list.append(
                        {
                            "x": float(entity.dxf.start.x),
                            "y": float(entity.dxf.start.y),
                            "alt": float(start_z),
                            "point_id": f"V{vertex_count}",
                        }
                    )
                    vertex_count += 1
                    coordinates_list.append(
                        {
                            "x": float(entity.dxf.end.x),
                            "y": float(entity.dxf.end.y),
                            "alt": float(end_z),
                            "point_id": f"V{vertex_count}",
                        }
                    )
                    vertex_count += 1

            elif entity.dxftype() == "CIRCLE":
                center_z = getattr(entity.dxf.center, "z", 0)
                if is_latlon:
                    coordinates_list.append(
                        {
                            "lat": float(entity.dxf.center.y),
                            "lon": float(entity.dxf.center.x),
                            "alt": float(center_z),
                            "point_id": f"V{vertex_count}",
                        }
                    )
                else:
                    coordinates_list.append(
                        {
                            "x": float(entity.dxf.center.x),
                            "y": float(entity.dxf.center.y),
                            "alt": float(center_z),
                            "point_id": f"V{vertex_count}",
                        }
                    )
                vertex_count += 1

            elif entity.dxftype() == "LWPOLYLINE" or entity.dxftype() == "POLYLINE":
                for vertex in entity.vertices():
                    z = vertex[2] if len(vertex) > 2 else 0
                    if is_latlon:
                        coordinates_list.append(
                            {
                                "lat": float(vertex[1]),
                                "lon": float(vertex[0]),
                                "alt": float(z),
                                "point_id": f"V{vertex_count}",
                            }
                        )
                    else:
                        coordinates_list.append(
                            {
                                "x": float(vertex[0]),
                                "y": float(vertex[1]),
                                "alt": float(z),
                                "point_id": f"V{vertex_count}",
                            }
                        )
                    vertex_count += 1

        return coordinates_list

    except Exception as e:
        print(f"Error parsing DXF file: {e}")
        return []
