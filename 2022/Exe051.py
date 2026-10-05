"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.

No final, mostre os 10 primeiros termos dessa progressão.
"""
termo = int(input('Primeiro termo: '))
razao = int(input('razao: '))
decimo_termo = termo + (10 - 1) * razao
for i in range(termo, decimo_termo, razao):
    print(f'{i}', end=' -> ')

print('Fim')
