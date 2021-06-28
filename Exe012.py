"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
"""
p = float(input('Preço: R$ '))
s = (p * 5) / 100
print(f'O novo preço é R${p - s}')