import pandas as pd
from tarefa1 import tabela_final

pagamentos_df = pd.read_excel('vendas.xlsx', sheet_name='Pagamentos')

pagos = pd.DataFrame(tabela_final[['Nome do Vendedor', 'Pagamento']].groupby('Nome do Vendedor', as_index=False).sum())

pagamentos_df = pagamentos_df.merge(pagos)

pagamentos_df = pagamentos_df[pagamentos_df['Comissão'] != pagamentos_df['Pagamento']]

pagamentos_df['Falta Pagar'] = pagamentos_df['Pagamento'] - pagamentos_df['Comissão']

print(pagamentos_df)