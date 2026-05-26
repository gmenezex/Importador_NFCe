from pathlib import Path
import os
import pandas as pd

def exportar_excel(serie, faltantes):
  dados = {
    'Serie': serie,
    'Inicial': faltantes,
    'Final': faltantes
  }
  df = pd.DataFrame(dados)
  df.to_excel('Faltantes.xlsx', index=False)
  print('Planilha para inutilização gerada com sucesso!')

def exportar_serie_e_sequencial(sequencial):
  if os.path.exists('Log_NFce.txt'):
    os.remove('Log_NFce.txt')

  for serie in sequencial.keys():
    with open('Log_NFce.txt', 'a', encoding='utf-8') as arquivo:
      arquivo.write(f'Serie importada: {serie}\n')
  
  for serie in sequencial:
    notas = sorted(sequencial.get(serie))
    faltantes = []
    for n in range(len(notas) -1):
      atual = notas[n]
      proximo = notas[n+1]

      numero = proximo - atual
      if numero > 1:
        for i in range(1, numero):
          faltantes.append(atual+i)
    with open('Log_NFce.txt', 'a', encoding='utf-8') as arquivo:
      arquivo.write('\n------------------------\n')
      arquivo.write(f'Serie: {serie} \nInicial: {sequencial.get(serie)[0]} | Final: {sequencial.get(serie)[-1]}\n')
      arquivo.write(f'Arquivos faltando: {len(faltantes)}\n')
      if len(faltantes) > 0:
        for falta in faltantes:
          arquivo.write(f'{falta}\n')
        exportar_excel(serie, faltantes)
      else:
        arquivo.write('Nenhum arquivo faltando para a serie \n')

def xmls_corrompidos(xml):
  if os.path.exists('Log_xmls.txt'):
    os.remove('Log_xmls.txt')
  with open("Log_xmls.txt", 'a', encoding='utf-8') as arquivo:
      arquivo.write(f"XML COM PROBLEMA OU VAZIO: {xml}\n")

