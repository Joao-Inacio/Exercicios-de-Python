"""
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
     o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
      então o empréstimo será negado.
"""
valor_casa = int(input('Qual o valor da casa? R$'))
salario = int(input('Salario R$'))
anos = int(input('Digite o numeros de parcelas: '))
parcelas = valor_casa / (anos * 12)
porcento = salario * 0.3


if parcelas >= porcento:
    print(f'A casa de R${valor_casa:.2f} com o salário de R${salario:.2f}'
          f' ficaria de parcelas de R${parcelas:.2f} imprestimo NEGADO')
else:
    print(f'A casa de R${valor_casa:.2f} com o salário de R${salario:.2f}'
          f' ficaria de parcelas de R${parcelas:.2f} imprestimo Aprovado')
