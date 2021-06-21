p = input('Escreva algo:')
print(f'é um digito {p.isdigit()}\n'
      f'é um número {p.isnumeric()}\n'
      f'é uma palavra {p.isalnum()}')
