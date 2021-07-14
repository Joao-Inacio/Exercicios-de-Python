"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""
nome = input('Digite seu nome completo: ').strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")}')
