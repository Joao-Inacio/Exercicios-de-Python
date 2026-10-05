p = input('Escreva algo:')
print(f'é um digito {p.isdigit()}\n'
      f'o tipo é {type(p)}\n'
      f'só tem espaços {p.isspace()}\n'
      f'é um número {p.isnumeric()}\n'
      f'é alfabético? {p.isalpha()}\n'
      f'Esta em maiúscula? {p.isupper()}\n'
      f'Esta em minúsculas? {p.islower()}\n'
      f'Está capitalizada? {p.istitle()}\n'
      f'é uma alfanumérico {p.isalnum()}')
