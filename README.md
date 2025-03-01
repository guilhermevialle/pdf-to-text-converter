# Conversor de memorial descritivo

## ✨ Por onde começar?
O primeiro passo é entender o **Problema C**.

---

## ⚙️ Funcionalidades

### 🔍 Problema A:
- Processamento de **memorial descritivo** nos formatos **.txt, .pdf ou imagem**;
- Verificação inicial para identificar se o **.pdf é digital** e legível, evitando processamento desnecessário;
- Conversão para **.txt de coordenadas, .dxf, .shp e .kml**;
- Armazenamento das coordenadas em **arrays**, permitindo ao usuário revisar e validar os pontos;
- Identificação do padrão de coordenadas no texto com entrada do usuário;
- Solicitação de informações necessárias para o algoritmo, como **padrões de conversão de dados**;
- **Validação das coordenadas** para evitar erros e garantir robustez.

### 🔒 Problema B:
- Mesmas funcionalidades do **Problema A**, mas **sem extração via OCR**, apenas a partir de **texto** contido no **.pdf**.

### 📏 Problema C:
- O usuário deve informar o **EPSG** do arquivo de entrada;
- Suporte para os seguintes formatos de entrada: **.txt, .dxf, .kml, .shp**;
- Opção para definir o tipo do memorial: **UTM, Lat/Lon, Azimute ou Rumo**;
- ~~Estruturação das coordenadas em objetos organizados com atributos como **nome, valor, etc**;~~
- Implementação de funções para:
  - **Cálculo de Azimute e Rumo** (armazenados em arrays);
  - **Cálculo de área e perímetro**;
- Conversão para **Memorial Descritivo (arquivo editável)**;
- Padrões suportados para memorial:
  - **SIGEF** (Texto corrido e tabular);
  - **Memorial de lote urbano**;
  - **Memorial simples** (arquivo editável).

---

## ⏳ Prioridades
- Aprimorar as funções para solicitar o **EPSG**;
- ~~Organizar os vértices dentro dos arrays em um formato de objeto estruturado com dados completos.~~
- Fazer a formatação do memorial descritivo para o formato SIGEF.
- ~~Estudar uma maneira de pegar os pontos no sentido horário e mais ao norte.~~
- Adicionar confrontantes entre os vértices. Ex: 1 - 5 = nome do confrontante.
- Variaveis opcionais: confrontantes, altura, nome do vertice;


## Confrontantes
- Criar uma interface para adicionar confrontantes entre os vértices. Ex:
(v1) - (v2) - [Nome do confrontante] - [Adicionar intervalo]
(v1) - (v2) - [Nome do confrontante] - [Adicionar intervalo]


---

## ✅ Testes
1. Testar imagens com **coordenadas UTM**;
2. Testar extração de texto em **.pdf**.

---

Este projeto visa facilitar a **extração e conversão de memoriais descritivos** para diversos formatos, garantindo precisão e flexibilidade para o usuário! 🚀

