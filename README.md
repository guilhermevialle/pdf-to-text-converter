# PDF to Text Extraction 📄➡️📝

Este projeto tem como objetivo converter arquivos PDF em imagens e extrair o texto das imagens geradas. Todos os arquivos de saída serão armazenados na pasta `dist`.

## Tecnologias utilizadas 🚀

- **Python**: Linguagem de programação para a implementação dos scripts.
- **poppler**: Ferramenta para conversão de PDF para imagem.

## Estrutura do projeto 📂

A estrutura do projeto é a seguinte:

```
.
├── dist/                  # Pasta de saída para imagens e textos extraídos
├── example.pdf            # Arquivo PDF de exemplo
├── img_to_text.py         # Módulo para extração de texto da imagem
├── pdf_to_img.py          # Módulo para conversão de PDF para imagem
├── main.py                # Script principal
└── README.md              # Documentação do projeto
```

## Requisitos 📋

Certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x**: A versão mais recente do Python.
- **poppler**: Biblioteca necessária para a conversão de PDF para imagem.

### Instalação do poppler no Windows 💻

No Windows, o poppler pode ser instalado facilmente utilizando o **Chocolatey**. Para isso, execute o seguinte comando no terminal do PowerShell:

```powershell
choco install poppler
```

## Como usar 🔧

Siga os passos abaixo para utilizar o projeto:

### 1. Instale as dependências necessárias

Execute o seguinte comando para instalar todas as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Execute o script principal

Após a instalação das dependências, execute o script principal para realizar a conversão de PDF para imagem e a extração de texto:

```bash
python main.py
```

## Configuração do script ⚙️

No arquivo `main.py`, defina os caminhos conforme a sua necessidade. Veja abaixo um exemplo de como o script pode ser configurado:

```python
import os
from pdf_to_img import convert_pdf_to_image
from img_to_text import extract_text_from_image

# Caminhos do arquivo PDF e pasta de saída
pdf_path = "example.pdf"
output_folder = "dist"
output_text_file = os.path.join(output_folder, "output.txt")
output_image_path = os.path.join(output_folder, "converted_pdf.jpg")

# Caminho do poppler (necessário no Windows)
poppler_path = r"C:\\ProgramData\\chocolatey\\lib\\poppler\\tools\\Library\\bin"

# Criação da pasta de saída, se não existir
os.makedirs(output_folder, exist_ok=True)

# Conversão do PDF para imagem
convert_pdf_to_image(pdf_path, output_image_path, poppler_path)

# Extração de texto da imagem gerada
text = extract_text_from_image(output_image_path, output_text_file)

# Exibindo o texto extraído
print("Texto extraído:\n", text)
```

## Saída esperada 🏁

Após a execução do script, os seguintes arquivos serão gerados na pasta `dist`:

- **`converted_pdf.jpg`**: Imagem gerada a partir do arquivo PDF.
- **`output.txt`**: Texto extraído da imagem.

## Contato 📧

Caso tenha alguma dúvida ou sugestão, entre em contato pelo e-mail: [dev.guilhermevialle@gmail.com](mailto:dev.guilhermevialle@gmail.com).

---

🏆 **Contribua!** Se você encontrou algum problema ou tem melhorias para sugerir, sinta-se à vontade para abrir uma **issue** ou **pull request**.