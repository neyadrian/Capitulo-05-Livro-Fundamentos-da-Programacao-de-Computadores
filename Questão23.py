#Faça um programa que receba o valor do salário mínimo, uma lista contendo a quantidade de quilowatts
#gasta por consumidor e o tipo de consumidor (1 — residencial; 2 — comercial; ou 3 — industrial)
#e que calcule e mostre:
    #■ o valor de cada quilowatt, sabendo que o quilowatt custa um oitavo do salário mínimo;
    #■ o valor a ser pago por consumidor (conta final mais acréscimo). O acréscimo encontra-se na tabela a seguir:
    #■ o faturamento geral da empresa;
    #■ a quantidade de consumidores que pagam entre R$ 500,00 e R$ 1.000,00.
#Termine a entrada de dados com quantidade de quilowats igual a zero.

sal : float 
qtd : int 
tipo : int 
valorKw : int 
gasto : int 
acresc : int 
total : int 
totGeral : int 
qtdCons : int 

totGeral = 0 
qtdCons = 0 

sal = float(input("Digite o salário: "))
qtd = int(input("Digite a quantidade: "))

valorKw = sal / 8 

while qtd != 0:
    gasto = qtd * valorKw 

    if tipo == 1:
        acresc = gasto * 5 / 100

    if tipo == 2:
        acresc = gasto * 10 / 100

    if tipo == 3:
        acresc = gasto * 15 / 100

    total = gasto + acresc 
    totGeral = totGeral + total 

    if total >= 500 and total <= 1000:
        qtdCons = qtdCons + 1 

    
    print(f"Gasto: {gasto}")
    print(f"Acrescimo: {acresc}")
    print(f"Total: {total}")

print(f"Total Geral: {totGeral}")
print(f"Quantidade de consumo: {qtdCons}")