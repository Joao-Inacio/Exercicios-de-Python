"""
 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tengente = math.tan(math.radians(angulo))
print(f'O Ângulo de {angulo} tem o Seno de {seno:.2f}\n'
      f'O Ângulo de {angulo} tem o Cosseno de {cosseno:.2f}\n'
      f'O Ângulo de {angulo} tem a Tangente de {tengente:.2f}\n')

