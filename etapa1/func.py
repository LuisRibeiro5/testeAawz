def limpa_reais(valor):
    valor = str(valor)
    valor = valor.replace('R$','').replace('.','').replace(',','.')

    return float(valor)

def comissao_mkt(linha):
    if linha['Canal de Venda'] == 'Online':
        linha['Comissao mkt'] = linha['Comissao'] * 0.2
    else:
        linha['Comissao mkt'] = 0

    return linha

def comissao_ger(linha):
    if linha['Comissao'] >= 1500:
        linha['Comissao ger'] = linha['Comissao'] * 0.1
    else:
        linha['Comissao ger'] = 0

    return linha
