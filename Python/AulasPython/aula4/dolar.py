#Este programa converte R$ em US$

reais = float(input("Qual o valor em reais? "))
dolarc = float(input("Qual a cotação do dolár? "))
valor = reais/dolarc
print(f"O valor de R${reais} em dólar é US${valor}")