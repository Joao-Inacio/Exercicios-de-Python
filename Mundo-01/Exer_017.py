from math import sqrt

cat_oposto = float(input("Comprimento do cateto oposto: "))
cat_adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = sqrt(pow(cat_oposto, 2) + pow(cat_adjacente, 2))
print(f"A hipotenusa vai medir { hipotenusa:.2f}")
