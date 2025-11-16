#Este programa calcula o IMC da pessoa

alt = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
IMC = peso / ( alt*alt )
print(f"Seu IMC é {IMC}.")