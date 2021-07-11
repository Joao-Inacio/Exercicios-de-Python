"""
 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
dos alunos e escrevendo na tela o nome do escolhido.
"""
import random
aluno1 = input('Nome do Primeiro Aluno: ')
aluno2 = input('Nome do Segundo Aluno: ')
aluno3 = input('Nome do Terceiro Aluno: ')
aluno4 = input('Nome do Quarto Aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sortea = random.choice(lista)
print(f'O aluno sorteado foi {sortea}')
