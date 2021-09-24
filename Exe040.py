"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Média {media} (abaixo de 5.0): REPROVADO')
elif 5 <= media <= 6.9:
    print(f'Média {media} (entre 5.0 e 6.9): RECUPERAÇÃO')
elif media >= 7:
    print(f'Média {media} (7.0 ou superior): APROVADO')
