"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
txt = "Inverter texto"[::-1]
print(txt) # otxet retrevnI
"""
frases = str(input("Digite uma frase: ")).strip().upper()
palavras = frases.split()
juntos = ''.join(palavras)
inverso = ''
for letra in range(len(juntos) - 1, -1, -1):
    inverso += juntos[letra]
print(f'O inverso de {juntos} é {inverso}')
if inverso == juntos:
    print('Temos um palíndromo')
else:
    print('Não Temos um palíndromo')
