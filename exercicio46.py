notas_alunos = {
    "Paulo": 8.5,
    "Caio": 9.0,
    "Izabel": 7.2,
    "Isa": 8.8}
aluno = input("Digite o nome do aluno: ")
nota = notas_alunos.get(aluno, "Aluno não encontrado")
print(f"A nota de {aluno} é: {nota}")