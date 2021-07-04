"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
 mostre quantos dólares ela pode comprar  1,00 = 3,27
"""
dinhero = float(input('Quantia de Dinheiro: R$'))
dolar = dinhero / 3.27
print(f'Você tem R${dinhero} e US${dolar:.2f}')

