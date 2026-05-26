from pathlib import Path
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

from xml_importacao import importar_arquivos_xml


def select_folder():
  # Abre a janela de explorer do windows para selecionar uma pasta.
  folder_path = filedialog.askdirectory(title='Selecione uma Pasta')

  # Se estiver com um caminho seleciona de pasta.
  if folder_path:
    input_folder.delete(0, ctk.END)
    input_folder.insert(0, folder_path)


def chamar_importar_xml():
  importar_arquivos_xml(input_folder.get(), info_area)


  # Parte visual para o usuário selecionar a pasta
root = ctk.CTk()
root.title('Importar arquivos NFCe')
root.geometry('450x450')

  # Label que vai apontar o caminho dos arquivos XMLs.
label_folder = ctk.CTkLabel(root, text='Seleciona a pasta')
label_folder.pack(pady=10)

  # Botão que vai abrir o explorer do windows para selecionar a pasta.
button_folder = ctk.CTkButton(root, text='Procurar Pasta', command=select_folder)
button_folder.pack(pady=10)

  # Campo de entrada, aonde vai ficar o caminho da pasta dos arquivos XMLs.
input_folder = ctk.CTkEntry(root, width=300, placeholder_text='Caminho da pasta selecionada')
input_folder.pack(pady=20, padx=20)

  # Botão para fazer a importação dos arquivos da pasta.
button_import = ctk.CTkButton(root, width=200, text='Importar XML NFce', fg_color='#487950', hover_color='green', command=chamar_importar_xml)
button_import.pack(pady=10)

  # Exibir informações na tela
info_area = ctk.CTkTextbox(root, width=300, height=300)
info_area.pack(pady=10)

root.mainloop()
