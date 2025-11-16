#Este programa calcula o aumento de 15% no salário

salario = float(input("Digite seu sálario: R$"))
conta = (salario*15) /100
aumento = salario + conta
print(f"Com aumento de 15%, seu salário será R${aumento}")