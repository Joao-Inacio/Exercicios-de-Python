"""
Faça um programa que leia a largura e altura de uma parede em metros calcule a sua área e a quantidade de
 tinta necessária para pintar lá sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
"""
altura = float(input('Altura?: '))
largura = float(input('Largura?: '))
metros = altura * largura
print(f'Uma parede de {metros}m vai precisar de {metros / 2}litros de tintas')

