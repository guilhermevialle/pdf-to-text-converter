
# Tipos de Coordenadas Suportados pelo Sistema

O sistema suporta dois tipos principais de coordenadas: **UTM** e **Latitude/Longitude**. Abaixo estão descritos os formatos esperados para cada tipo de coordenada.

---

## Coordenada UTM

A estrutura de uma coordenada no formato UTM é definida como um objeto com os seguintes campos:

```json
{
  "x": float,           // Coordenada E/X em metros (ex: 458123.45)
  "y": float,           // Coordenada N/Y em metros (ex: 7198234.56)
  "alt": float,         // Altitude em metros, opcional (ex: 832.5)
  "point_id": str       // Identificador do ponto (ex: 'V1', 'M1')
}
```

### Descrição dos Campos:
- **x**: Representa a coordenada Este (Easting) ou X em metros.
- **y**: Representa a coordenada Norte (Northing) ou Y em metros.
- **alt** *(opcional)*: Representa a altitude em metros.
- **point_id**: Identificador único do ponto, geralmente representado por uma string (ex: `'V1'`, `'M1'`).

---

## Coordenada Latitude/Longitude

A estrutura de uma coordenada no formato Latitude/Longitude é definida como um objeto com os seguintes campos:

```json
{
  "lat": float,         // Latitude em graus decimais (ex: -23.550520)
  "lon": float,         // Longitude em graus decimais (ex: -46.633308)
  "alt": float,         // Altitude em metros, opcional (ex: 832.5)
  "point_id": str       // Identificador do ponto (ex: 'V1', 'M1')
}
```

### Descrição dos Campos:
- **lat**: Representa a latitude em graus decimais. Valores negativos indicam localizações no hemisfério sul.
- **lon**: Representa a longitude em graus decimais. Valores negativos indicam localizações a oeste do Meridiano de Greenwich.
- **alt** *(opcional)*: Representa a altitude em metros.
- **point_id**: Identificador único do ponto, geralmente representado por uma string (ex: `'V1'`, `'M1'`).

---

### Observações Importantes:
1. O campo `alt` (altitude) é **opcional** em ambos os formatos. Caso não seja fornecido, assume-se que a altitude não está disponível ou não é relevante.
2. O campo `point_id` deve ser uma string única para identificar cada ponto no sistema.
3. Certifique-se de fornecer valores válidos para as coordenadas, respeitando os limites geográficos e as unidades de medida especificadas.

