import pandas 

# serie = pandas.Series([10, 20, 30]) # Estrutura unidimensional - vetor
# dados = {
#     'nome': ['Ana', 'Bia', 'Carlos'],
#     'idade': [30, 10, 18]
# }

# df = pandas.Dataframe(dados) # Estrutura bidimensional - natriz

# print(serie)

ler_base = pandas.read_csv('Df_analise.CSV' , sep=';')
print(ler_base)

print(pandas.DataFrame(ler_base))

print(ler_base.dropna()) # Remove  todas as linhas que tem pelo menos um NaN.

print(ler_base.dropna(axis=1, how= 'all')) # Remove colunas vazias 'axis=1' e 'axis=0' remove linhas.

print(ler_base.describe()) # Mostra estatísticas básicas.

print(ler_base.loc[1]) # 

print(ler_base.loc[1, 'Nome']) #

print(ler_base.iloc[1, 2]) #

