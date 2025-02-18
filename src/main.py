# Importação dos analisadores de arquivo
from utils.parsers.kml_parser import kml_parser
from utils.parsers.shp_parser import shp_parser
from utils.parsers.dxf_parser import dxf_parser

# Importações do Tkinter para interface gráfica
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Importação das abas da aplicação
from tabs.file_to_memorial_tab import FileToMemorialTab
from tabs.memorial_to_file import MemorialToFileTab


# Função para obter o analisador apropriado com base no tipo de arquivo
def get_parser(file_type):
    # Dicionário que mapeia extensões de arquivo para seus respectivos analisadores
    parsers = {"kml": kml_parser, "shp": shp_parser, "dxf": dxf_parser}
    return parsers.get(file_type)


class App:
    def __init__(self, root):
        # Inicialização da janela principal
        self.root = root
        self.root.title("Conversor de documentos geoespaciais")
        self.root.minsize(540, 480)
        self.root.maxsize(800, 600)

        # Criação do notebook (container de abas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Inicialização da aba de memorial descritivo
        self.memorial_tab = FileToMemorialTab(self.notebook)
        # Inicialização da aba de exemplo
        self.example_tab = MemorialToFileTab(self.notebook)


def main():
    # Criação e inicialização da aplicação
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
