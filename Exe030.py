"""
     Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
     ou ÍMPAR.
"""
n = int(input('Digite um número: '))
print(f'O Número {n} é Par' if n % 2 == 0 else f'O Número {n} é Ímpar')
