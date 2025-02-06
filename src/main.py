from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser
from utils.indetifiers.index import file_identifier
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils.transformers.index import utm_to_latlon, latlon_to_utm
from constants.reference import epsg
from utils.boilerplate import boilerplate


# Função para obter o analisador apropriado com base no tipo de arquivo
def get_parser(file_type):
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Coordenadas")
        self.root.geometry("540x400")
        self.coordinates = None
        self.coord_type = tk.StringVar(value="latlon")

        # Criar notebook para abas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Aba Memorial
        self.memorial_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.memorial_tab, text="Gerar Memorial")

        # Aba Exemplo
        self.example_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.example_tab, text="Exemplo")

        # Configurar aba Memorial
        main_frame = ttk.Frame(self.memorial_tab, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Botão para selecionar arquivo
        self.select_button = ttk.Button(
            main_frame,
            text="Selecionar Arquivo (KML, SHP/ZIP ou DXF)",
            command=self.select_file,
        )
        self.select_button.pack(pady=10)

        # Frame para os radio buttons
        radio_frame = ttk.Frame(main_frame)
        radio_frame.pack(pady=5)

        # Radio buttons para escolher o formato de exibição
        ttk.Radiobutton(
            radio_frame,
            text="Lat/Lon",
            variable=self.coord_type,
            value="latlon",
            command=self.update_display,
        ).pack(side=tk.LEFT, padx=5)

        ttk.Radiobutton(
            radio_frame,
            text="UTM",
            variable=self.coord_type,
            value="utm",
            command=self.update_display,
        ).pack(side=tk.LEFT, padx=5)

        # Área de texto para exibir resultados
        self.result_area = tk.Text(main_frame, height=20, width=80)
        self.result_area.pack(fill=tk.BOTH, expand=True, pady=10)

        # Configurar aba Exemplo
        example_frame = ttk.Frame(self.example_tab, padding="10")
        example_frame.pack(fill=tk.BOTH, expand=True)

        # Botão exemplo
        self.example_button = ttk.Button(
            example_frame,
            text="Botão de Exemplo",
            command=lambda: messagebox.showinfo(
                "Exemplo", "Este é um botão de exemplo!"
            ),
        )
        self.example_button.pack(pady=10)

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

    def update_display(self):
        if not self.coordinates:
            return

        self.result_area.delete(1.0, tk.END)

        if self.coord_type.get() == "latlon":
            display_coords = utm_to_latlon(self.coordinates, epsg)
        else:
            display_coords = latlon_to_utm(self.coordinates, epsg)

        self.result_area.insert(
            tk.END, f"Coordenadas no formato {self.coord_type.get().upper()}:\n\n"
        )
        self.result_area.insert(tk.END, boilerplate(display_coords))

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
            self.coordinates = parser(file_path)

            # Verifica se foram encontradas coordenadas
            if not self.coordinates:
                messagebox.showinfo(
                    "Informação", "Nenhuma coordenada encontrada no arquivo."
                )
                return

            # Atualiza a exibição com base no formato selecionado
            self.update_display()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao analisar o arquivo: {e}")


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
