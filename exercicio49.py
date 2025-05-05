# Utilizando a função items()
notas_alunos = {
    "Paulo": 8.5,
    "Caio": 9.0,
    "Izabel": 7.2,
    "Isa": 8.8}
for aluno, nota in notas_alunos.items():
    print(f"Aluno: {aluno}, Nota: {nota}")