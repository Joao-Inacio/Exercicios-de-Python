"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por
dia e R$0,15 por Km rodado.
"""
km = float(input('Quantos Km rodados: '))
dia = int(input("Quantos dia foi alugado: "))
total = (dia * 60) + (km * 0.15)
print(f'Você percorreu {km}Km em {dia} Dias o total a pagar é de R${total}')
