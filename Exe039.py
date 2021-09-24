"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime
ano_atual = datetime.datetime.now().year
ano_cadidato = int(input('Qual o seu ano de nascimento: '))
idade = ano_atual - ano_cadidato


if idade < 18:
    print(f'você tem {idade}  ainda falta {idade - 18} anos para se alistar ao serviço militar')
elif idade == 18:
    print('É a hora exata de se alistar')
else:
    print(f'você tem {idade} já passou {idade - 18} anos  do alistamento')


