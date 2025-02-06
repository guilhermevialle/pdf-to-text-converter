import zipfile
import shapefile
import os


# Função para descompactar arquivos .zip contendo arquivos .shp
# zip_path: caminho do arquivo .zip
# extract_to: diretório onde os arquivos serão extraídos (padrão: "temp_shp")
# Retorna o caminho do arquivo .shp extraído ou None em caso de erro
def unzip_shp(zip_path: str, extract_to: str = "temp_shp") -> str:
    try:
        os.makedirs(extract_to, exist_ok=True)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)

        for file in os.listdir(extract_to):
            if file.lower().endswith(".shp"):
                return os.path.join(extract_to, file)

        return None

    except Exception as e:
        print(f"Error unzipping file: {e}")
        return None


# Função para verificar e processar o arquivo de entrada
# file_path: caminho do arquivo (.shp ou .zip)
# extract_to: diretório para extrair arquivos .zip (padrão: "temp_shp")
# Retorna o caminho do arquivo .shp válido ou None se inválido
def shp_verifier(file_path: str, extract_to: str = "temp_shp") -> str:
    if file_path.lower().endswith(".zip"):
        shp_file = unzip_shp(file_path, extract_to)
        if not shp_file:
            return None
        return shp_file

    elif file_path.lower().endswith(".shp"):
        return file_path

    else:
        print(f"Unsupported file format. Please provide .shp or .zip file")
        return None


# Função para analisar e extrair coordenadas de um arquivo shapefile
# file_path: caminho do arquivo shapefile (.shp) ou arquivo zip contendo shapefile
# Retorna uma lista de dicionários contendo as coordenadas dos vértices
# Cada dicionário contém:
# - lat/lon ou x/y: coordenadas do ponto dependendo do sistema de coordenadas
# - alt: altitude (0 se não especificada)
# - point_id: identificador único do vértice (V1, V2, etc)
def shp_parser(file_path: str) -> list:
    try:
        if file_path.lower().endswith(".shp"):
            verified_path = file_path
        else:
            verified_path = shp_verifier(file_path, "temp_shp")

        if not verified_path:
            return []

        sf = shapefile.Reader(verified_path)
        coordinates_list = []
        vertex_count = 1

        coordinates_system = sf.shapeTypeName

        for shape in sf.shapes():
            for point in shape.points:
                x, y = point[:2]
                alt = point[2] if len(point) > 2 else 0

                if coordinates_system.lower() in ["latlon", "geographic"]:
                    coordinates_list.append(
                        {"lat": y, "lon": x, "alt": alt, "point_id": f"V{vertex_count}"}
                    )
                else:
                    coordinates_list.append(
                        {
                            "x": x,
                            "y": y,
                            "alt": alt,
                            "point_id": f"V{vertex_count}",
                        }
                    )
                vertex_count += 1
        return coordinates_list

    except Exception as e:
        print(f"Error parsing shapefile: {e}")
        return []
