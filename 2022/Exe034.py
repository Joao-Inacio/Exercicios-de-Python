"""
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
     superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual o Salário R$'))
if salario >= 1250.00:
    print(f'Seu novo salário é de R${salario + (salario * 10) / 100}')
else:
    print(f'Seu novo salário é de R${salario + (salario * 15) / 100}')

