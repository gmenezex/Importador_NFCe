# Importador de NFC-e

Aplicação em Python para processamento automatizado de XMLs de NFC-e, responsável por calcular o total de vendas e cancelamentos. Possui geração de logs para identificar quebras de sequencial numérico (Log_NFce.txt) e apontar arquivos corrompidos menores que 1 KB (Log_xmls.txt).

Arquivos com quebra de sequencial geram uma planilha com a série e o sequencial faltante para importação e inutilização automatizada em outros softwares, eliminando o trabalho manual. Além disso, a ferramenta conta com um sistema de correção de encoding, que detecta e repara automaticamente arquivos XML que apresentam falhas de caracteres especiais ou acentuação, evitando o travamento da leitura.

---

## 🚀 Principais Tecnologias e Bibliotecas Utilizadas

O projeto foi construído utilizando Python e destaca-se pelo uso das seguintes soluções:

### 🎨 Interface Gráfica (GUI)
* **`customtkinter`**
* **`darkdetect`**
* **`colorama`**

### 📊 Processamento e Manipulação de Dados
* **`pandas` & `numpy`:** 
* **`openpyxl` & `et_xmlfile`:** 


### ⚙️ Utilitários
* **`tqdm`:** 

## 📋 Pré-requisitos

Se você for executar o projeto diretamente pelo código-fonte, precisará do **Python 3.10+** instalado e das dependências listadas requirements.txt.

