"""
 Faça um algoritmo que leia o salário de um funcionário e mostre o novo 
 salário com 15% de aumento
"""
sala_inicial = float(input('Salário inicial: R$'))
novo_sala = sala_inicial + (sala_inicial * 15) / 100
print(f'Seu novo salário é de R${novo_sala:.2f}')
