op= input('Digite um número de 1 a 7')
print({
    '1': 'Segunda',
    '2': 'Terça',
    '3': 'Quarta',
    '4': 'Quinta',
    '5': 'Sexta',
    '6': 'Sábado',
    '7': 'Domingo',}.get(op, 'Opção inválida'))