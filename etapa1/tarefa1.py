import pandas as pd
from func import *

vendas_df = pd.read_excel('vendas.xlsx')


vendas_df['Comissao'] = vendas_df['Valor da Venda'].apply(limpa_reais) * 0.1

vendas_df = vendas_df.apply(comissao_mkt, axis=1)

vendas_df = vendas_df.apply(comissao_ger,axis=1)

vendas_df['Pagamento'] = vendas_df['Comissao'] - vendas_df['Comissao mkt'] - vendas_df['Comissao ger']

tabela_final = vendas_df[['Nome do Vendedor','Comissao', 'Pagamento']]
