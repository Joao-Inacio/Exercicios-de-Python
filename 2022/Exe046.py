"""
        Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep

print("23:50 Dez segundo para o fim de ano")

for i in range(10, -1, -1):
    sleep(1)
    print(i)
    if i == 0:
        print(f'parapapa')
        sleep(2)
        print(f'parapapa')
        sleep(2)
        print(f'parapapa')
        sleep(3)
        print(f'pow')

