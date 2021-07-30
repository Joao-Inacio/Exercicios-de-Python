"""
    Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
     por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
distancia = float(input('Distância da viagem em Km: '))
if distancia <= 200:
    print(f'Você ira começar um viagem de {distancia}Km.\n'
          f'Sua passagem custará R${distancia * 0.50}')
else:
    print(f'Você ira começar um viagem de {distancia}Km.\n'
          f'Sua passagem custará R${distancia * 0.45}')
