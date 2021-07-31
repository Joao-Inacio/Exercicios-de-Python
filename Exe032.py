"""
     Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date
# Minha resolução
ano = int(input('Digite um ano ou 0 para o ano atual: '))
               # a parti daqui vi na aula
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano de {ano} é ano bissexto')
else:
    print(f'O Ano {ano} não é bissexto')
