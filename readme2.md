# Memorial Extractor

**Descrição**
O *Memorial Extractor* é uma ferramenta destinada a extrair, converter e manipular coordenadas geoespaciais a partir de arquivos em diferentes formatos. O objetivo é facilitar a conversão de memorial descritivo em texto para formatos geoespaciais e vice-versa, realizando validações e oferecendo funcionalidades para cálculos de área, perímetro, azimute, e rumo.

## Funcionalidades

### Problema A - Extração Completa:
- **Leitura de Arquivos**: Suporta arquivos .txt, .pdf (digital legível) e imagens.
    - *Nota*: Arquivos PDF digitalizados (imagens) são analisados para verificação de legibilidade, evitando sobrecarga de processamento.
- **Conversão de Formatos**: Converte as coordenadas extraídas para formatos .txt, .dxf, .shp e .kml.
- **Armazenamento de Coordenadas**: As coordenadas extraídas são armazenadas em arrays para posterior verificação e ajustes pelo usuário.
- **Identificação de Padrão**: O usuário define o padrão no texto para localizar as coordenadas.
- **Personalização de Algoritmos**: O usuário fornece informações como padrões de conversão e validação para as coordenadas.
- **Validação de Coordenadas**: Implementação robusta para validar as coordenadas e evitar erros.

### Problema B - Extração Simples:
- **Leitura de Arquivos**: Suporta apenas a extração de texto de arquivos .pdf, sem o uso de OCR.
- **Conversão de Formatos**: Converte as coordenadas para .txt, .dxf, .shp e .kml, sem a necessidade de OCR.

### Problema C - Manipulação e Cálculos:
- **Entrada de EPSG**: O usuário deve informar o código EPSG do arquivo de entrada para garantir a correta transformação e referência espacial.
- **Formatos de Entrada**: Suporte para .txt, .dxf, .kml e .shp.
- **Padrões de Memorial**: O usuário escolhe entre os tipos de memorial: UTM, LatLon, azimute ou rumo.
- **Armazenamento de Coordenadas**: Criação de objetos com informações detalhadas sobre cada coordenada (ex.: nome, valor, etc.).
- **Funções de Cálculo**:
    - Cálculo de azimute e rumo.
    - Cálculo de área e perímetro.
- **Geração de Memorial Descritivo**: Converte os dados em memorial descritivo editável, nos padrões SIGEF (texto corrido e tabular), memorial de lote urbano ou memorial simples.

## Prioridades
- Melhorar as funções de solicitação do EPSG para entrada de coordenadas.
- Organizar os vértices das coordenadas em arrays de objetos contendo dados relevantes (nome, valor, etc.).

## Testes
- **Testar com Arquivos UTM**: Validar a conversão e manipulação de arquivos com sistema de referência UTM.
- **Testar com Arquivos PDF**: Validar a extração de texto a partir de arquivos PDF.

