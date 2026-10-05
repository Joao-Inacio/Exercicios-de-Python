"""
    Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
     de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""
nu = int(input('Digite um número inteiro: '))
print('Escolha uma das basses para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL \n'
      '[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{nu} convertido para BINÁRIO é igual a {bin(nu)[2:]}')
    pass
elif escolha == 2:
    print(f'{nu} convertido para OCTAL é igual a {oct(nu)[2:]}')
elif escolha == 3:
    print(f'{nu} convertido para HEXADECIMAL é igual a {hex(nu)[2:]}')
else:
    print('opção invalida')

