import os
# Essa função pega os arquivos xmls de venda, verifica se tem evento de cancelamento e altera o status.
# Depois ele pega os valores filtrando por status.
def verificar_xml(xmls, xmls_cancelados, info_area):
  for xml in xmls:
    if xml['Chave'] in xmls_cancelados:
      xml['Status'] = False

  valor_cancelados = sum([xml['Valor'] for xml in xmls if xml['Status'] == False])
  valor_vendas = sum([xml['Valor'] for xml in xmls if xml['Status'] == True])
  valor_total = valor_vendas - valor_cancelados


  valor_cancelados = str(f'{valor_cancelados:,.2f}').replace(",", "X").replace(".", ",").replace("X", ".")
  valor_vendas = str(f'{valor_vendas:,.2f}').replace(",", "X").replace(".", ",").replace("X", ".")
  valor_total = str(f'{valor_total:,.2f}').replace(",", "X").replace(".", ",").replace("X", ".")

  info_area.delete("0.0", "end")
  info_area.insert('0.0', 
  f'''
  Quantidade Vendas: {len(xmls)}
  Valor vendas: R$ {valor_vendas}
  ----------------------------------------------
  Quantidade Cancelados: {len(xmls_cancelados)}
  Valor cancelados: R$ {valor_cancelados}
  ----------------------------------------------
  Total de XMLs: {len(xmls_cancelados) + len(xmls)}
  Valor total: R$ {valor_total}
''')