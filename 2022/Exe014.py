"""
Escreva um programa que converta uma temperatura digitada °C e converta para °F
"""
temperatura = float(input('Temperatura atual: '))
converso = temperatura * 1.8 + 32
print(f'A Temperatura {temperatura}°C  vai ficar {converso:.1f}°F')
