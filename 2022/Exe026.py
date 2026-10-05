"""
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
  aparece a primeira vez e em que posição ela aparece a última vez.
"""
frase = input('Digite uma Frase: ').strip()
novo_a = str(frase).lower()
print(f"A letra A aparece {novo_a.count('a')} vezes na frase.\n"
      f"A primeria letra A apareceu na posição {novo_a.find('a')+1}\n"
      f"A última letra A apareceu na posição {novo_a.rfind('a')+1}")
