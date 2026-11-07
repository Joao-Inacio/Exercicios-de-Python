from random import sample

alunos = []
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)
alunos.append(aluno4)
print(sample(alunos, k=len(alunos)))
