"""
     Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
      ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input('Velocidade atual do veiculo: '))
if velocidade > 80:
    print(f'Excesso de velocidade, você foi multado em R${(velocidade - 80) *7}  ')
else:
    print(f'Velocidade Normal continui assim')

