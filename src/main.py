from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser
from utils.indetifiers.index import file_identifier
import json
from constants.reference import epsg


def get_parser(file_type):
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


def main():
    print("Por favor, insira o caminho do seu arquivo (KML, SHP/ZIP ou DXF):")
    file_path = input().strip()
    file_type = file_identifier(file_path)

    if not file_type:
        print(
            "Erro: Formato de arquivo não suportado. Por favor, use arquivos KML, SHP/ZIP ou DXF"
        )
        return

    # Obtém o analisador apropriado
    parser = get_parser(file_type)

    if not parser:
        print("Erro: Não foi possível encontrar um analisador apropriado.")
        return

    # Analisa as coordenadas
    try:
        coordinates = parser(file_path, epsg)

        if not coordinates:
            print("Nenhuma coordenada encontrada no arquivo.")
            return

        print(f"\nCoordenadas encontradas no formato {file_type.upper()}:")
        print(json.dumps(coordinates, indent=2))

    except Exception as e:
        print(f"Erro ao analisar o arquivo: {e}")


if __name__ == "__main__":
    main()
