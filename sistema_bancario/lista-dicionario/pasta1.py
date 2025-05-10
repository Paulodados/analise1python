# # Lista
# estados_lista = ['SP', 'RJ', 'MG']
# print(estados_lista[1]) #RJ
# estados_lista[1] = 'SC'
# print(estados_lista) #  SP, SC, MG
# estados_lista.append('AC')
# print(estados_lista) # SP, SC, MG, AC
# estados_lista.insert(2, 'ES ')
# print(estados_lista) # SP, SC, MG, AC
# estados_lista.remove('SP')
# print(estados_lista) # SC, ES, MG, AC
# estados_lista.pop(1)
# print(estados_lista) # SC, MG, AC

# # Tupla
# estados_tupla = ('SP', 'RJ', 'RJ')
# print(estados_tupla[1]) # RJ
# estados_tupla[1] = 'SC' # ERRO - tuplas são imuaveis
# estados_tupla.append('SC') # ERRO
# estados_tupla.remove('SP') # ERRO


# # Set
# estados_set = {'SP', 'RJ', 'MG'}
# print(estados_set[1]) # ERRO
# estados_set.add('SC') # SP, SC, RJ, MG
# estados_set.add('RJ') # ERRO - não permite duplicadas
# estados_set.remove('SP') # RJ, SC, MG


# # Dicionário
# estados_dict = {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}
# print(estados_dict['RJ']) # Rio de Janeiro
# estados_dict['RJ'] = 'RioJaneiro'
# print(estados_dict) # {'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}
# estados_dict["nome"] = 'ana'
# print(estados_dict) # 'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais' 'nome': 'ana' }


#1- Armazene 5 frutas nas 4 estruturas.
#- lista
# valores = []

# #- estrutura de repetição
# for i in range(5):
#     valor = input(f'Digite o {i+1} item:° ')
#     valores.append(valor)

# #- armazenamento (lista, tupla, set, dict)
lista = list(dados)
tupla = tuple(dadoos)
conjunto = set(dados)
#dicionario = dict(valores) # Erro - Dicionario precisa de dois elementos chave/valor
dicionario2 = {j: valor for j, valor in enumerate(dados)}

#- print
print('Lista: ', lista)
print('Tupla: ', tupla)
print('Conjunto:', conjunto)
#print('Dicionario: ', dicionario)
print('Dicionario 2: ', dicionario2)


#2- Faça o mesmo que o exrcício anterior, mas com valores randômicos do tipo inteiro.
#- faça o import random
import random

def gerar_dados(qtd, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(qtd)]

print('Lista aleatória:\n')
dados = gerar_dados(5, 1, 22) 
# print(lista) 

lista = list(dados)
tupla = tuple(dados)
conjunto = set(dados)
#dicionario = dict(valores) # Erro - Dicionario precisa de dois elementos chave/valor
dicionario = {j: dados for j, dados in enumerate(dados)}

#- print
print('Lista: ', lista)
print('Tupla: ', tupla)
print('Conjunto:', conjunto)
#print('Dicionario: ', dicionario)
print('Dicionario : ', dicionario)






############################### Lista, Tupla, Set, Dicionário
#-Acesso por índice: Lista, Dicionário, Tupla,
#-Alterável: Lista, Dicionário, set
#-Permite duplicados: Lista, Tupla,
#-Ordenado: Lista, Dicionário, Tupla,

# #-X
# lista2 = ['maçã', 'banana', 'uva']

# #-Y
# tupla2 =('maçã', 'banana', 'uva')

# #-W
# conjunto2 = {'maçã', 'banana', 'uva'}

# #-Z
# dicionario2 = {'nome': 'João', 'idade': 30, 'cidade': 'SP'}