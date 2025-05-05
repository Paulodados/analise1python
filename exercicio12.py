def temperatura(op, t):
  return {
      '1': (t * 9/5) + 32,
      '2': t + 273.15
  }.get(op, 'Opção inválida')

op= input('Digite a conversão desejada: 1-Celsius para Fahrenheit, 2-Celsius para Kelvin:')
t = float(input('Digite a temperatura Celsius: '))
print('Temperatura convertida: ', temperatura(op, t))