#Etapa 1

##Tarefa 1

**Primeiro passo** foi colocar o arquivo excel em uma váriavel para começar a manipulação.

- Coluna comissão
Criei uma função para limpar e converter para float todos os valores das vendas dos funcionários, onde essa funcao foi aplicada na coluna 'Valor da Venda'.
Depois criei uma nova coluna 'Comissao' onde esta recebeu o Calculo da comissao de 10% de acordo com o que cada pessoa teve em 'Valor da Venda'.

- Colunas comissão ger/mkt
Após isso criei duas funções, uma para calcular a comissao que o time de marketing teria e outra para a comissao do gerente.
Então criei uma nova coluna 'Comissao mkt' e passei os valores para coluna de acordo com as condições da função *'comissao_mkt'* que recebe uma linha como argumento.
Realizei operação parecida para a coluna da *'Comissao ger'*, onde dessa vez apliquei a função específica para calcular a comissão do gerente.

- Tabela final
Com essas 3 colunas calculadas, consegui fazer a operação para descobrir o valor a ser pago para cada funcionário.

Por fim, criei a *'tabela_final'* que mostra os resultados obtidos na tabela.

##Tarefa 2

Primeiro passei a tabela 'Pagamentos' para uma veriável pagamentos_df.

Criei então uma tabela *'pagos'*, onde eu agrupei por nome as colunas 'Nome do Vendedor' e 'Pagamento', da *'tabela final'*. 

E então realizei um merge na tabela pagamentos_df passando a tabela 'pagos', relacionando oque foi pago e o correto a ser pago.

Após isso removi as linhas que o pagamento estava correto.

Depois calculei a diferença do ainda necessitaria de ser pago aos funcionários, apontado na coluna *"Falta Pagar"* da tabela *'pagamentos_df'*

###Para visualizar a tabela de comissões é necessário abrir a pasta em uma ide,entrar na pasta etapa1, e executar o arquivo tarefa1. E para visulizar a tabela de pagamentos executar o arquivo tarefa2.


#Etapa 2

Na etapa 2, para conseguir extrair os nomes dos socios e sua quantidade de cotas utilizei regex.
Onde filtrei em cada linha nome e cotas.
No nome fiz uma condição, onde caso um nome fosse filtrado pelo regex ele passaria por uma função de "limpeza", chamada 'corrige nome'. 
E após eu adicionava o nome em uma lista nomes, e cota em uma lista cotas.

Criei então um dicionário, para conseguir criar um dataframe e poder mostra a tabela com nome e cotas de cada sócio.

###para visualizar a tabela de Nome e cotas dos sócios é necessário abrir a pasta em uma ide, e entrando na pasta 'etapa2' executar o arquivo 'main.py'.
