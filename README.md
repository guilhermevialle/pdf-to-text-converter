# Memorial extractor

Por onde comecar? Pelo problema C.

## Features
### Problema A:
- Pegar um memorial descritivo em .txt, .pdf, ou imagem (Primeiro analisar se eh um .pdf digital legivel para evitar carga de processamento);
- Converter para .txt de coordenadas, para .dxf, .shp e .kml;
- Salvar cada coordenada em Arrays, para questionar ao usuario os valores de cada ponto;
- Pedir para o usuario identificar o padrao no texto para extrair as coordenadas;
- Pedir informações necessarias para o funcionamento do algoritmo (patterns para conversao de dados);
- Validar coordenadas para evitar erros (solucao robusta)

### Problema B:
As mesmas features porem sem extracao via OCR, apenas via extracao de texto do .pdf

### Problema C:
- Usuario deve informar o EPSG do arquivo de entrada;
- Inputs: .txt, .dxf, .kml, .shp;
- Escolher: O memorial pode ser UTM, LatLon, azimute ou rumo;
- Criar um objeto com informacoes para cada coordenada para arrays (nome, valor, etc);
- Funcoes: calcular azimute e rumo - armazenar em array, calcular area e perimetro;
- Transformar em: Memorial descritivo (arquivo editavel);
- Os padroes do memorial vao ser: SIGEF - Texto corrido e tabular, Memorial de lote urbano e memorial simples (arquivo editavel)


### Prioridades:
- Melhorar funcoes para pedir EPSG;
- Organizar os vertices dentro dos Arrays em formato de objeto com dados;

### Testes
- 1. Testar imagens com UTM
- 2. Testar com .pdf

