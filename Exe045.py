"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import choice


print("""
    Pedra | Papel | Tesoura \n""")

pc = ['Pedra', 'Papel', 'Tesoura']
escolha = choice(pc)

usuario = input('Sua escolha: ')

if escolha == 'Pedra' and usuario.upper() == 'TESOURA':
    print(f'O pc escolheu {escolha} e ganhou')
elif escolha == 'Papel' and usuario.upper() == 'PEDRA':
    print(f'O pc escolheu {escolha} e ganhou')
elif escolha == 'Tesoura' and usuario.upper() == 'PAPEL':
    print(f'O pc escolheu {escolha} e ganhou')
elif usuario.upper() == 'PEDRA' and escolha == 'Tesoura':
    print(f'O pc escolheu {escolha} e você ganhou')
elif usuario.upper() == 'PAPEL' and escolha == 'Pedra':
    print(f'O pc escolheu {escolha} e você ganhou')
elif usuario.upper() == 'TESOURA' and escolha == 'Papel':
    print(f'O pc escolheu {escolha} e você ganhou')
elif escolha == usuario.upper():
    print(f'O pc escolheu {escolha} e deu inpate')

