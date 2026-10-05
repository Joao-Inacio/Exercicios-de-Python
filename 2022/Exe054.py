"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores.
"""
pessoas = []
p = 1
while True:
    pessoa = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    pessoas.append(pessoa)
    p += 1
    if len(pessoas) == 7:
        break

ma = 0
me = 0

for i in pessoas:
    s = i - 2022
    if (s * -1) < 18:
        me += 1
    else:
        ma += 1

print(f'Ao todo tivimos {ma} pessoas maiores de idade')
print(f'E também tivemos {me} pessoas menores de idade')
