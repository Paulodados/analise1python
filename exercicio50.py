notas_alunos = {
    "Paulo": 8.5,
    "Caio": 9.0,
    "Izabel": 7.2}
aluno = input("Digite o nome do aluno: ")
if aluno in notas_alunos:
    print(f"A nota de {aluno} é: {notas_alunos[aluno]}")
else:
    print("Aluno não encontrado.")