#Este programa calcula a média do aluno e mostra se ele foi ou não aprovado

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Dgite a segunda nota: "))
média = float((n1 + n2)/2)
print(f"Média: {média}")
print("Aprovado?", média >= 6)
