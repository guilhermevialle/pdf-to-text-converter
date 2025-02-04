# Memorial extractor

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
- Inputs: .txt, .dwg, .kml, .shp, .dxf;
- Transformar em: Memorial descritivo (arquivo editavel);
- O memorial pode ser UTM, LatLon, azimute ou rumo;
- Os padroes do memorial vao ser: SIGEF - Texto corrido e tabular, Memorial de lote urbano e memorial simples (arquivo editavel)

## Testes
- 1. Testar imagens com UTM
- 2. Testar com .pdf

