#Faça um programa que receba o salário de um funcionário chamado Carlos. Sabe-se que outro funcionário,
#João, tem salário equivalente a um terço do salário de Carlos. Carlos aplicará seu salário
#integralmente na caderneta de poupança, que rende 2% ao mês, e João aplicará seu salário integralmente
#no fundo de renda fixa, que rende 5% ao mês. O programa deverá calcular e mostrar a
#quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor
#pertencente a Carlos.

salCarlos : float 
salJoao : float 
meses : int 

salCarlos = float(input("Digite o salário de Carlos: "))

salJoao = salCarlos / 3 

meses = 0 

while salJoao < salCarlos:
    salCarlos = salCarlos + (salCarlos * 2 / 100)
    salJoao = salJoao + (salJoao * 5 / 100)
    meses = meses + 1 

print(f"Meses: {meses}")