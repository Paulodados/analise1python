#Variavél inicial.
string = input('Digite uma string: ')
vogais = 'aeiouAEIOU'
#Variavél de cálculo.
for letra in string:
  if letra in vogais:
    print(letra)