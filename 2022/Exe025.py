"""
 Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome
"""
nome = input('Qual é seu nome completo: ').lower()
n1 = nome.count('silva')
n2 = str(n1)
print(f"Seu nome tem Silva? {n2 == '1'}")
