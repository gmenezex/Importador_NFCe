import os
import xml.etree.ElementTree as ET
from dados_da_importacao import verificar_xml
from pathlib import Path
from exportacao_de_dados import exportar_serie_e_sequencial, xmls_corrompidos
from tqdm import tqdm


def valida_xml(arquivo, caminho, xmls_venda, xmls_cancelados, sequencial):
  caminho_com_arquivo = f'{caminho}\\{arquivo}'
  tamanho_xml = os.path.getsize(f'{caminho_com_arquivo}')
  tamanho_xml = tamanho_xml / 1024

  if tamanho_xml <= 1:
    xmls_corrompidos(arquivo)
  else:
    try:
      tree = ET.parse(caminho_com_arquivo)
      root = tree.getroot()
      ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

      # Pegando pelo evento o xml cancelado e acessando sua chave.
      if root.tag == '{http://www.portalfiscal.inf.br/nfe}procEventoNFe':
        chave = root.find('.//nfe:chNFe', ns)
        xmls_cancelados.append(chave.text)

      # Pegando pelo evento o xml de venda e seus valores.
      elif root.tag == '{http://www.portalfiscal.inf.br/nfe}nfeProc':
        chave = root.find('.//nfe:chNFe', ns)
        serie = root.find('.//nfe:serie', ns)
        num_nota = root.find('.//nfe:nNF', ns)
        
        preco = root.find('.//nfe:vNF', ns)
        dados_xml = {
          'Chave': chave.text,
          'Serie': serie.text,
          'Nota': int(num_nota.text),
          'Valor': float(preco.text),
          'Status': True
        }

        xmls_venda.append(dados_xml)

        # O sistema está pegando a serie das notas fiscais e colocando os números de notas emitidas.
        if serie.text not in sequencial:
          sequencial[serie.text] = [int(num_nota.text)]

        else:
          sequencial[serie.text].append(int(num_nota.text))

      pass
    except Exception as e:
      arquivo_xml = Path(f'{caminho_com_arquivo}')
      conteudo = arquivo_xml.read_bytes()
      conteudo = conteudo.replace(b'encoding="UTF-8"', b'encoding="ISO-8859-1"')
      arquivo_xml.write_bytes(conteudo)
      valida_xml(arquivo,caminho,xmls_venda, xmls_cancelados, sequencial)


def importar_arquivos_xml(caminho, info_area):
  arquivos_xml = os.listdir(caminho)

  xmls_venda = []
  xmls_cancelados = []
  sequencial = {}

  for xml in tqdm(arquivos_xml):
    valida_xml(xml, caminho, xmls_venda, xmls_cancelados, sequencial)

  verificar_xml(xmls_venda, xmls_cancelados,info_area)
  exportar_serie_e_sequencial(sequencial)

  if os.path.exists('Log_NFce.txt'):
    os.startfile('Log_NFce.txt')
  if os.path.exists('Log_xmls.txt'):
    os.startfile('Log_xmls.txt')
