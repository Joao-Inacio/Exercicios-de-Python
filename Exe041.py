"""
 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
 categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
from datetime import datetime

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos e é um atleta MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos e é um atleta INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos e é um atleta JÚNIOR')
elif idade <= 25:
    print(f'Você tem {idade} anos e é um atleta SÊNIOR')
elif idade > 25:
    print(f'Você tem {idade} anos e é um atleta MASTER')
else:
    print('Coloque uma data valida e tente novamente')
