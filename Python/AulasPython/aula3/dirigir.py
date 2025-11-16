#Este programa mostra sea pessoa pode dirigir

idade = int(input("Você tem quantos anos? "))
tem_cnh = input("Você tem CNH? (s/n): ").lower()

if idade >= 18 and tem_cnh == "s":
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")