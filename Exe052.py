"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número
primo.
"""
n = int(input('Digite um número: '))
pri = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='')
        pri += 1
    else:
        print('\033[m', end='')
    print(f' {i} ', end='')
print(f'\nO número {n} foi divisível {pri} vazes')
print('Número PRIMO' if pri == 2 else 'Número não é primo')
