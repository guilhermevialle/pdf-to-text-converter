from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser
from utils.indetifiers.index import file_identifier
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


# Função para obter o analisador apropriado com base no tipo de arquivo
def get_parser(file_type):
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Coordenadas")
        self.root.geometry("420x340")

        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Botão para selecionar arquivo
        self.select_button = ttk.Button(
            main_frame,
            text="Selecionar Arquivo (KML, SHP/ZIP ou DXF)",
            command=self.select_file,
        )
        self.select_button.pack(pady=10)

        # Área de texto para exibir resultados
        self.result_area = ScrolledText(main_frame, height=20, width=80)
        self.result_area.pack(fill=tk.BOTH, expand=True, pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Selecione o arquivo",
            filetypes=[
                ("Todos os formatos", "*.kml;*.shp;*.zip;*.dxf"),
                ("Arquivos KML", "*.kml"),
                ("Arquivos SHP/ZIP", "*.shp;*.zip"),
                ("Arquivos DXF", "*.dxf"),
            ],
        )

        if not file_path:
            return

        self.process_file(file_path)

    def process_file(self, file_path):
        # Limpa a área de resultado
        self.result_area.delete(1.0, tk.END)

        # Identifica o tipo do arquivo
        file_type = file_identifier(file_path)

        # Verifica se o tipo de arquivo é suportado
        if not file_type:
            messagebox.showerror(
                "Erro",
                "Formato de arquivo não suportado. Por favor, use arquivos KML, SHP/ZIP ou DXF",
            )
            return

        # Obtém o analisador apropriado para o tipo de arquivo
        parser = get_parser(file_type)

        # Verifica se foi possível encontrar um analisador
        if not parser:
            messagebox.showerror(
                "Erro", "Não foi possível encontrar um analisador apropriado."
            )
            return

        # Tenta analisar as coordenadas do arquivo
        try:
            # Executa o parser e obtém as coordenadas
            coordinates = parser(file_path)

            # Verifica se foram encontradas coordenadas
            if not coordinates:
                messagebox.showinfo(
                    "Informação", "Nenhuma coordenada encontrada no arquivo."
                )
                return

            # Exibe as coordenadas encontradas
            self.result_area.insert(
                tk.END, f"Coordenadas encontradas no formato {file_type.upper()}:\n\n"
            )
            self.result_area.insert(tk.END, json.dumps(coordinates, indent=2))

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao analisar o arquivo: {e}")


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
