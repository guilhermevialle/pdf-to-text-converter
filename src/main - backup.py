from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser
from utils.indetifiers.index import file_identifier
import json


# Função para obter o analisador apropriado com base no tipo de arquivo
def get_parser(file_type):
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


def main():
    # Solicita o caminho do arquivo ao usuário
    print("Por favor, insira o caminho do seu arquivo (KML, SHP/ZIP ou DXF):")
    file_path = input().strip()

    # Identifica o tipo do arquivo
    file_type = file_identifier(file_path)

    # Verifica se o tipo de arquivo é suportado
    if not file_type:
        print(
            "Erro: Formato de arquivo não suportado. Por favor, use arquivos KML, SHP/ZIP ou DXF"
        )
        return

    # Obtém o analisador apropriado para o tipo de arquivo
    parser = get_parser(file_type)

    # Verifica se foi possível encontrar um analisador
    if not parser:
        print("Erro: Não foi possível encontrar um analisador apropriado.")
        return

    # Tenta analisar as coordenadas do arquivo
    try:
        # Executa o parser e obtém as coordenadas
        coordinates = parser(file_path)

        # Verifica se foram encontradas coordenadas
        if not coordinates:
            print("Nenhuma coordenada encontrada no arquivo.")
            return

        # Exibe as coordenadas encontradas
        print(f"\nCoordenadas encontradas no formato {file_type.upper()}:")
        print(json.dumps(coordinates, indent=2))

    except Exception as e:
        print(f"Erro ao analisar o arquivo: {e}")


if __name__ == "__main__":
    main()
