import re


def extrair_coordenadas(texto):
    resultados = []
    # Regex que encontra coordenadas (E/N), GMS e azimutes
    padrao = r"(?:[A-Z]{1,3}\d+\s*(?:coordenadas:)?\s*E\s*=\s*([\d\.,]+)\s*m;\s*N\s*=\s*([\d\.,]+)\s*m)|(?:[A-Z]{1,3}\d+\s*N\s*([\d\.,]+)\s*m\s*e\s*E\s*([\d\.,]+)\s*m)|(?:GMS\s*([\d°\s']+)\s*,\s*([\d°\s']+))|(?:azimute\s*([\d°\s']+))"

    for match in re.finditer(padrao, texto):
        if match.group(1):  # Coordenadas E/N
            e = match.group(1).replace(".", "").replace(",", ".")
            n = match.group(2).replace(".", "").replace(",", ".")
            resultados.append({"tipo": "coordenadas", "E": float(e), "N": float(n)})
        elif match.group(3):  # Coordenadas N/E
            n = match.group(3).replace(".", "").replace(",", ".")
            e = match.group(4).replace(".", "").replace(",", ".")
            resultados.append({"tipo": "coordenadas", "E": float(e), "N": float(n)})
        elif match.group(5):  # GMS
            latitude = match.group(5).strip()
            longitude = match.group(6).strip()
            resultados.append(
                {"tipo": "gms", "latitude": latitude, "longitude": longitude}
            )
        elif match.group(7):  # Azimute
            azimute = match.group(7).strip()
            resultados.append({"tipo": "azimute", "valor": azimute})

    return resultados


# Exemplos de texto com diferentes identificadores de vértice
texto1 = """

Split by PDF Splitter
O IMÓVEL
Natureza do imóvel: ÁREA URBANA
Localização: AV. BARÃO DO RIO BRANCO, 409
Município: TEIXEIRAS-MG
Matrícula no C.R.I.: 775
Área Total: 9.564,15 m2
Finalidade: RETIFICAÇÃO DE ÁREA
Proprietários: CONCEIÇÃO ALVIM e OUTROS
Utilização: PLENO DOMÍNIO
DESCRIÇÃO
110
FRENTE:
66,04 m para a AV. BARÃO DO RIO BRANCO entre os vértices V1 (coordenadas: E = 723361,36 m; N = 7714531,26 m) e V2 (coordenadas: E = 723344,01 m; N = 7714594,97 m) e azimute de 344°45'59".
LATERAL DIREITA:
63,42 m limita-se com o lote de ANTÔNIO CARLOS MARTINS entre os vértices V2 e V3 (coordenadas: E = 723388,61 m; N = 7714640,05 m) e azimute de 44°41'33".
31,86 m limita-se com a margem esquerda do córrego entre os vértices V3 e V8 na seguinte ordem: Do vértice V3 segue-se pela montante córrego até o vértice V4 (coordenadas: E = 723392,18 m; N = 7714636,29 m) com azimute 136°31'19" e distância de 5,19 m.
Do vértice V4 segue-se pela montante córrego até o vértice V5 (coordenadas: E = 723394,10 m; N = 7714628,87 m) com azimute 165°29'32" e distância de 7,66 m.
Do vértice V5 segue-se pela montante córrego até o vértice V6 (coordenadas: E = 723396,84 m; N = 7714625,29 m) com azimute 142°34'54" e distância de 4,51 m.
Do vértice V6 segue-se pela montante córrego até o vértice V7 (coordenadas: E = 723403,61 m; N = 7714620,85 m) com azimute 123°14'46" e distância de 8,09 m.
Do vértice V7 segue-se pela montante do córrego até o vértice V8 (coordenadas: E = 723405,82 m; N = 7714614,83 m) com azimute 159°47'32" e distância de 6,41 m.
1,52 m atravessa-se o córrego entre os vértices V8 e V9 (coordenadas: E = 723407,34 m; N = 7714614,95 m) e azimute 85°40'42".
60,80 m limita-se com o lote de AIRTON JOSÉ DE FREITAS e OUTROS entre os vértices V9 e V12 na seguinte ordem:
Do vértice V9 segue-se até o vértice V10 (coordenadas: E = 723412,29 m; N = 7714617,32 m) com azimute 64°24'39" e distância de 5,49 m.
Do vértice V10 segue-se até o vértice V11 (coordenadas: E = 723427,80 m; N = 7714620,53 m) com azimute 78°18'22" e distância de 15,83 m.
Do vértice V11 segue-se até o vértice V12 (coordenadas: E = 723467,04 m; N = 7714624,84 m) com azimute 83°44'1" e distância de 39,48 m.
FUNDOS:
66,16 m limita-se com a extinta R.F.F.S.A. entre os vértices V12 e V13 (coordenadas: E = 723473,44 m; N = 7714558,99 m) e azimute 174°26'45".
LATERAL ESQUERDA
Página | 1
Augus
Número do documento: 20123116330500000001885767184
https://pje.tjmg.jus.br.443/pje/Processo/Consulta Documento/listView.seam?x=20123116330500000001885787184 Assinado eletronicamente por: Vinicius De Paula Fernandes - 31/12/2020 18:19:26
MG
Num. 1888039798 - Pág. 4
"""

texto2 = """

Split by PDF Splitter
36,88 m limita-se com o lote dos herdeiros de IRACEMA MEDINA FLORESTA entre os vértices V13 e V17 na seguinte ordem:
Do vértice V13 segue-se pela cerca até o vértice V14 (coordenadas: E = 723458,89 m; N = 7714550,75 m) com azimute 240°29'26" e distância de 16,73 m.
Do vértice V14 segue-se pela cerca até o vértice V15 (coordenadas: E = 723453,50 m; N = 7714546,41 m) com azimute 231°5'46" e distância de 6,92 m.
Do vértice V15 segue-se pela cerca até o vértice V16 (coordenadas: E = 723445,54 m; N = 7714542,97 m) com azimute 246°40'13" e distância de 8,67 m.
Do vértice V16 segue-se pela cerca até o vértice V17 (coordenadas: E = 723441,07 m; N = 7714542,09 m) com azimute 258°53'23" e distância de 4,56 m.
1,50 m atravessa-se o córrego entre os vértices V17 e V18 (coordenadas: E = 723439,60 m; N = 7714541,75 m) e azimute 256°53'58".
2,18 m limita-se com a margem esquerda do córrego entre os vértices V18 e V19 na seguinte ordem:
Do vértice V18 segue-se pela montante do córrego até o vértice V19 (coordenadas: E = 723441,00 m; N = 7714540,09 m) com azimute 140°4'23".
90,25 m limita-se com o lote de AVAIR DIAS entre os vértices V19 e V1 (início desta descrição) na seguinte ordem:
Do vértice V19 segue-se até o vértice V20 (coordenadas: E = 723417,82 m; N = 7714533,87 m) com azimute 254°59'51" e distância de 24,00 m.
Do vértice V20 segue-se pelo muro até o vértice V21 (coordenadas: E = 723413,71 m; N = 7714545,23 m) com azimute 340°6'44" e distância de 12,07 m.
Do vértice V21 segue-se pelo muro até o vértice V1 com azimute 255°3'36" e distância de 54,18 m. Todas as coordenadas aqui descritas estão GEO-REFERENCIADAS ao SISTEMA GEODÉSICO BRASILEIRO e encontram-se representadas no sistema UTM, tendo como referência o Meridiano Central -45°00'00" WGr, e o Datum o SIRGAS 2000. Os azimutes e distancias, área e perímetro foram calculados no plano de projeção UTM.
Contém nesta área 2 (duas) casas residenciais como se vê representadas na planta do levantamento topográfico a qual ora anexo.
Teixeiras(MG), 02 de maio de 2.018
hugio Auques to laufferings
SERGIO AUGUSTO MACIEL PEREIRA
ENGENHEIRO AGRIMENSOR-CREA-MG 36.476/D
Página | 2
Número do documento: 20123116330500000001885767184
https://pje.tjmg.jus.br.443/pje/Processo/Consulta Documento/listView.seam?x=20123116330500000001885787184 Assinado eletronicamente por: Vinicius De Paula Fernandes - 31/12/2020 18:19:26
Num. 1888039798 - Pág. 5
"""

print(extrair_coordenadas(texto1))
print(extrair_coordenadas(texto2))
