# Importações do Tkinter para interface gráfica
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Importações de utilitários para transformação de coordenadas
from utils.transformers.index import utm_to_latlon, latlon_to_utm
from constants.reference import epsg
from utils.boilerplate import boilerplate
from utils.indetifiers.index import file_identifier

# Importações dos analisadores de arquivos
from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser


# Função para obter o analisador apropriado com base no tipo de arquivo
def get_parser(file_type):
    # Dicionário que mapeia extensões de arquivo para seus respectivos analisadores
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


class FileToMemorialTab:
    def __init__(self, notebook):
        # Inicialização das variáveis de estado
        self.coordinates = None  # Armazena as coordenadas processadas
        self.coord_type = tk.StringVar(value="latlon")  # Tipo de coordenada selecionado

        # Criação da aba principal
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Gerar Memorial")

        # Configuração do frame principal com padding
        main_frame = ttk.Frame(self.tab, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Botão para seleção de arquivo
        self.select_button = ttk.Button(
            main_frame,
            text="Selecionar Arquivo (KML, SHP/ZIP ou DXF)",
            command=self.select_file,
        )
        self.select_button.pack(pady=10)

        # Frame para os botões de rádio
        radio_frame = ttk.Frame(main_frame)
        radio_frame.pack(pady=5)

        # Botões de rádio para escolha do formato de coordenadas
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

        # Frame para área de texto e botão
        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Área de texto para exibição dos resultados
        self.result_area = tk.Text(text_frame, height=10)
        self.result_area.pack(fill=tk.X, expand=False)

        # Botão para copiar o texto
        self.copy_button = ttk.Button(
            text_frame,
            text="Copiar Memorial",
            command=self.copy_text,
            state=tk.DISABLED,
        )
        self.copy_button.pack(pady=5)

    def copy_text(self):
        # Copia o texto da área de resultado para a área de transferência
        text = self.result_area.get(1.0, tk.END).strip()
        self.tab.clipboard_clear()
        self.tab.clipboard_append(text)
        messagebox.showinfo("Sucesso", "Memorial copiado para a área de transferência!")

    def select_file(self):
        # Abre diálogo para seleção de arquivo com filtros específicos
        file_path = filedialog.askopenfilename(
            title="Selecione o arquivo",
            filetypes=[
                ("Todos os formatos", "*.kml;*.shp;*.zip;*.dxf"),
                ("Arquivos KML", "*.kml"),
                ("Arquivos SHP/ZIP", "*.shp;*.zip"),
                ("Arquivos DXF", "*.dxf"),
            ],
        )

        # Verifica se um arquivo foi selecionado
        if not file_path:
            return

        # Processa o arquivo selecionado
        self.process_file(file_path)

    def update_display(self):
        # Verifica se existem coordenadas para exibir
        if not self.coordinates:
            return

        # Limpa a área de texto
        self.result_area.delete(1.0, tk.END)

        # Converte as coordenadas para o formato selecionado
        if self.coord_type.get() == "latlon":
            display_coords = utm_to_latlon(self.coordinates, epsg)
        else:
            display_coords = latlon_to_utm(self.coordinates, epsg)

        # Exibe as coordenadas no formato selecionado
        self.result_area.tag_configure("bigger", font=("TkDefaultFont", 10, "normal"))
        self.result_area.insert(tk.END, boilerplate(display_coords), "bigger")
        self.result_area.configure(padx=8, pady=8)

        # Habilita o botão de copiar quando houver texto para copiar
        self.copy_button.config(state=tk.NORMAL)

    def process_file(self, file_path):
        # Limpa a área de resultado antes de processar novo arquivo
        self.result_area.delete(1.0, tk.END)
        # Desabilita o botão de copiar
        self.copy_button.config(state=tk.DISABLED)

        # Identifica o tipo do arquivo selecionado
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

        # Verifica se existe um analisador disponível
        if not parser:
            messagebox.showerror(
                "Erro", "Não foi possível encontrar um analisador apropriado."
            )
            return

        # Processa o arquivo e extrai as coordenadas
        try:
            # Executa o parser no arquivo selecionado
            self.coordinates = parser(file_path)

            # Verifica se foram encontradas coordenadas no arquivo
            if not self.coordinates:
                messagebox.showinfo(
                    "Informação", "Nenhuma coordenada encontrada no arquivo."
                )
                return

            # Atualiza a exibição com as novas coordenadas
            self.update_display()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao analisar o arquivo: {e}")
