"""
 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

n = input('Nome de uma cidade: ').lower()
n1 = n.count('santo')
n2 = str(n1)
print(n2 == '1')

# Resolução

"""cidade = str(input('Nome da cidade: ')).split()
tem_santo = str(cidade[:5]).upper()
print(tem_santo == 'SANTO')"""
