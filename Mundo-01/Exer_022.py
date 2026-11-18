nome = str(input("Digite seu nome completo: "))

nome_maiuscula = nome.upper()
nome_minuscula = nome.lower()
nome_sem_espaco = len(nome.replace(' ', ''))
primeiro_nome = nome.split()

print(f"Nome em maiúsculas: {nome_maiuscula}")
print(f"Nome em minúsculas: {nome_minuscula}")
print(f"Seu nome tem {nome_sem_espaco}  (sem considerar espaços). ")
print(f"Seu primeiro nome tem {len(primeiro_nome[0])} letras. ")
