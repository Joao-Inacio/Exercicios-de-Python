"""
    Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
    triângulo.
"""
p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmento acima Podem Formar triângulo')
else:
    print('Os segmento acima NÃO podem formar um triângulo')
