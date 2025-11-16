#Este programa calcula a média de 3 notas 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
média = float( n1 + n2 + n3 ) /3
print(f"A média do aluno é {média: .2f}")