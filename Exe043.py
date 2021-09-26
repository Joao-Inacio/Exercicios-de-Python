"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu
status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

altura = float(input('Qual a sua altura: '))
peso = float(input('Qual o seu peso: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é de ({imc:.2f}) = Abaixo do Peso')
elif imc < 25:
    print(f'Seu IMC é de ({imc:.1f}) = Peso Ideal')
elif imc < 30:
    print(f'Seu IMC é de ({imc:.1f}) = Sobrepeso')
elif imc < 40:
    print(f'Seu IMC é de ({imc:.1f}) = Obesidade')
elif imc > 40:
    print(f'Seu IMC é de ({imc:.1f}) = Obesidade Mórbida')
else:
    print('Altura ou peso invalido tente novamente.')
