
def soma(a, b):
    if a % 2 != 0 or b % 2 != 0:
       raise ValueError('Um dos valores é impar')
    return a + b

# print(soma(5, 2))
try:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    resultado = soma(a, b)
except ValueError as ve:
    print('Erro:' , ve)
except Exception as e:
    print(' Erro inesperado! ' , e)    
else:
    print('soma = ', resultado)
finally:
    print('Fim do par!')        



