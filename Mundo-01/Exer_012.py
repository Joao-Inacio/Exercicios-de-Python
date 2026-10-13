preco = float(input("Qual o preço do produto: R$"))

desconto = preco - ((preco * 5) / 100)
print(f"O produto que custava R${preco}, na promoção com desconto de 5% vai custa R${desconto:.2f}")
