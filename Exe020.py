"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
 que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random
aluno1 = input('Nome do Primeiro Aluno: ')
aluno2 = input('Nome do Segundo Aluno: ')
aluno3 = input('Nome do Terceiro Aluno: ')
aluno4 = input('Nome do Quarto Aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem vai ser \n'
      f'{lista}')
