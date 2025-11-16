#Este programa mostra o preço do produto com 10% de desconto

preco = float(input("Qual o preço do produto? "))
desconto = float(preco*10) /100
valor = float(preco-desconto)
print(f"Com 10% de desconto o preço será R${valor}")