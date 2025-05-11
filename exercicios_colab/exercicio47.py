
notas_alunos = {
    "Paulo": 8.5,
    "Caio": 9.0,
    "Izabel": 7.2}
novo_aluno = input("Digite o nome do novo aluno: ")
nova_nota = float(input("Digite a nota do aluno: "))
notas_alunos[novo_aluno] = nova_nota
print(notas_alunos)