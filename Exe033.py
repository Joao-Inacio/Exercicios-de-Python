"""
     Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior')
elif n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior')
elif n3 > n1 and n3 > n1:
    print(f'O número {n3} é o maior')
if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor')
elif n2 < n1 and n2 < n3:
    print(f'O número {n2} é o menor')
elif n3 < n1 and n3 < n1:
    print(f'O número {n3} é o menor')
