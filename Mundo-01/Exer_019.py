import random

alunos = []
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)
alunos.append(aluno4)
print(f"O aluno escolhido foi {alunos[random.randint(0, (len(alunos) - 1))]}")
print(len(alunos)-1)
