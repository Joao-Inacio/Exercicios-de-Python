"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
import math
# ou from math import trunc
n = float(input('Digite um número: '))
novo = math.trunc(n)
print(f'O valor inteiro de {n} é {novo}')


