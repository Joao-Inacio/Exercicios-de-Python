"""
    Refaça o DESAFIO 9, mostrando
    a tabuada de um número
    que o usuário escolher,
    só que agora utilizando um laço for
"""

n = int(input('Digite Um número: '))
c = 0
for i in range(11):
    print(f'{n} X {c} = {n * c}')
    c += 1
