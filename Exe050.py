"""
    Desenvolva um programa que leia seis
    números inteiros e mostre a soma
    apenas daqueles que forem pares.
    Se o valor digitado for ímpar, desconsidere-o.
"""
s = 0
c = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}° valor: '))
    if n % 2 == 0:
        s += n
        c += 1

print(f'você informou {c} números e a soma deles foi {s}')
