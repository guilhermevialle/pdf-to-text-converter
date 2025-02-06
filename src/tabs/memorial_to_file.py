import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class MemorialToFileTab:
    def __init__(self, notebook):
        # Aba Exemplo
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Gerar arquivo")

        # Configurar aba Exemplo
        example_frame = ttk.Frame(self.tab, padding="10")
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
