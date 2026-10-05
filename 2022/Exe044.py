"""
 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
 pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""

preco = float(input('Preço do produto: R$'))
print("""Qual a forma de pagamento:
[ 1 ] A vista/ cheque
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")
opcao = int(input('Sua opção: '))

if opcao == 1:
    percetual = 10.0 / 100.0
    valor_final = preco - (percetual * preco)
    print(f'A sua compra de R${preco} saiu com disconto por R${valor_final}')
elif opcao == 2:
    percetual = 5.0 / 100.0
    valor_final = preco - (percetual * preco)
    print(f'A sua compra de R${preco} saiu com disconto por R${valor_final}')
elif opcao == 3:
    print(f'A sua compra de R${preco} saiu  por R${preco}')
elif opcao == 4:
    percetual = 20.0 / 100.0
    valor_final = preco + (percetual * preco)
    parcela = int(input('Quantas parcelas: '))
    print(f'A sua compra de R${preco} saiu por R${valor_final}\n'
          f'em {parcela}x de R${valor_final / parcela}')
else:
    print('valor ou opção invalida.')
