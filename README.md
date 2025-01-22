# PDF to Text Extraction

Este projeto tem como objetivo converter arquivos PDF em imagens e extrair o texto das imagens geradas. Todos os arquivos de saída serão armazenados na pasta `dist`.

## Tecnologias utilizadas

- **Python**
- **poppler** (para conversão de PDF para imagem)

## Estrutura do projeto

```
.
├── dist/                  # Pasta de saída para imagens e textos extraídos
├── example.pdf            # Arquivo PDF de exemplo
├── img_to_text.py         # Módulo para extração de texto da imagem
├── pdf_to_img.py          # Módulo para conversão de PDF para imagem
├── main.py                # Script principal
└── README.md              # Documentação do projeto
```

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- poppler (pode ser instalado via Chocolatey no Windows)

No Windows, o poppler pode ser instalado com o comando:
```powershell
choco install poppler
```

## Como usar

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script principal:
   ```bash
   python main.py
   ```

## Configuração do script

No arquivo `main.py`, defina os caminhos conforme a necessidade:

```python
import os
from pdf_to_img import convert_pdf_to_image
from img_to_text import extract_text_from_image

pdf_path = "example.pdf"
output_folder = "dist"
output_text_file = os.path.join(output_folder, "output.txt")
output_image_path = os.path.join(output_folder, "converted_pdf.jpg")
poppler_path = r"C:\\ProgramData\\chocolatey\\lib\\poppler\\tools\\Library\\bin"

os.makedirs(output_folder, exist_ok=True)
convert_pdf_to_image(pdf_path, output_image_path, poppler_path)
text = extract_text_from_image(output_image_path, output_text_file)

print("Texto extraído:\n", text)
```

## Saída esperada

Os arquivos gerados estarão na pasta `dist`:

- `converted_pdf.jpg`: imagem gerada do PDF
- `output.txt`: texto extraído da imagem

## Contato

Caso tenha alguma dúvida ou sugestão, entre em contato pelo e-mail: `dev.guilhermevialle@gmail.com`.

