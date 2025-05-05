# Utilizando a função .upper e .append
nomes = []

lista_nomes = int(input('Digite quantidade de nomes: '))

for i in range(lista_nomes):
  nome = input(f'Digite o {i+1}º nome da lista: ')
  nomes.append(nome)

nomes_maiusculos = [nome.upper() for nome in nomes]

print(nomes_maiusculos)
