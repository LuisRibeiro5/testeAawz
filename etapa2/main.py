from docx import Document
import re
import pandas as pd

def corrige_nome(nome):
    return nome.replace(',','').replace('.','')

arquivo = Document('Partnership.docx')
nome_re = re.compile(r'\. [A-Z][a-zá-ú]+ [A-Z][a-zá-ú]+,')
cotas_re = re.compile(r'[0-9]{1,2} cotas?')

nomes = []
cotas = []

for paragrafo in arquivo.paragraphs:
    linha1 = paragrafo.text 
    nome = nome_re.findall(linha1)
    cota = cotas_re.findall(paragrafo.text)
    
    if nome and cota:
        nomes.append(corrige_nome(nome[0]))
        cotas += cota 

   
dados = {
    'Nomes': nomes,
    'Cotas': cotas
}

tabela = pd.DataFrame(dados)

print(tabela)
