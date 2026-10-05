"""
 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""
nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print(f'Muito prazer {n[0]}\n'
      f'Seu primeiro nome é {n[0]}\n'
      f'Seu último nome é {n[len(n)-1]}')
