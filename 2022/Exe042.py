"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferente
"""
p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if p1 == p2 == p3:
    print('Forma um triângulo EQUILÁTERO: todos os lados iguais')
elif p1 == p2 or p1 == p3 or p2 == p3:
    print('Forma um triângulo ISÓSCELES: dois lados iguais, um diferente')
elif p1 != p2 or p1 != p3 or p2 != p3:
    print('Forma um triângulo ESCALENO: todos os lados diferente')
else:
    print('Os segmento acima NÃO podem formar um triângulo')
