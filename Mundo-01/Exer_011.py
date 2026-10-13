altura = float(input("Altura da parede: "))
largura = float(input("Largura da parede: "))

area = altura * largura
litros = area / 2
print(f"Sua parede tem a dimesão {altura} x {largura} e sua área é de {area}m².")
print(f"Para pinta essa parede, você vai precisar de {litros}l de tinta.")
