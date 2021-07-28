"""
    Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
     descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
      venceu ou perdeu.
"""
from random import randint

numero_oculto = randint(0, 5)
print(numero_oculto)
numero_usuario = int(input('Digite o número da sorte: '))
if numero_usuario == numero_oculto:
    print(f'O seu número {numero_usuario} foi correto')
else:
    print('Que pena, tente outra vez')
