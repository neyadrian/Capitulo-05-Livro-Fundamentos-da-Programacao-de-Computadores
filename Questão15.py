#Faça um programa que receba o preço unitário, a refrigeração (S para os produtos que necessitem de
#refrigeração e N para os que não necessitem) e a categoria (A — alimentação; L — limpeza; e V —
#vestuário) de doze produtos, e que calcule e mostre:
    #■ O custo de estocagem, calculado de acordo com a tabela a seguir.
    #■ O imposto calculado de acordo com as regras a seguir:
#Se o produto não preencher nenhum dos requisitos a seguir, seu imposto será de 2% sobre o preço
#unitário; caso contrário, será de 4%.
#Os requisitos são: categoria — A e refrigeração — S.
    #■ O preço final, ou seja, preço unitário mais custo de estocagem mais imposto.
    #■ A classificação calculada usando a tabela a seguir.
    #■ A média dos valores adicionais, ou seja, a média dos custos de estocagem e dos impostos dos doze produtos.
    #■ O maior preço final.
    #■ O menor preço final.
    #■ O total dos impostos.
    #■ A quantidade de produtos com classificação barato.
    #■ A quantidade de produtos com classificação caro.
    #■ A quantidade de produtos com classificação normal.

i : int 
preco : int 
custoEst : int 
imp : int 
precoFinal : int 
adicional : int 
maiorP : int 
menorP : int 
totImp : int 
qtdB : int 
qtdN : int 
qtdC : int 
refri : str 
categ : str 

adicional = 0  
totImp = 0 
qtdB = 0
qtdN = 0 
qtdC = 0

for i in range(1, 12):
    preco = int(input("Digite o preço: "))
    refri = int(input("Digite a refrigeração: "))
    categ = input("Digite a categoria: ")
    
    if preco <= 20:
        if categ == "A":
            custoEst = 2 
        if categ == "L":
            custoEst = 3
        if categ == "V":
            custoEst = 4 

    if preco > 20 and preco <= 50:
        if refri == "S":
            custoEst = 6
        else:
            custoEst = 0

    if preco > 50:
        if refri == "S":
            if categ == "A":
                custoEst = 5
            if categ == "L":
                custoEst = 2
            if categ == "V":
                custoEst = 4 
    else:
        if categ == "A" or categ == "V":
            custoEst = 0
        if categ == "L":
            custoEst = 1

if categ != "A" and refri != "S":
    imp = preco * 2 / 100
else:
    imp = preco * 4 / 100

precoFinal = preco + custoEst + imp 

print(f"Cust Est: {custoEst}")
print(f"Imp: {imp}")
print(f"Preço final: {precoFinal}")

if precoFinal <= 20:
    qtdB = qtdB + 1 
    print("Clasificação Barato")
if precoFinal > 20 and precoFinal <= 100:
    qtdN = qtdN + 1
    print("Classificação Normal")
if precoFinal > 100:
    qtdC = qtdC + 1 
    print("Classificação Caro")

adicional = adicional + custoEst + imp 
totImp = totImp = imp 

if i == 1:
    maiorP = precoFinal
    menorP = precoFinal 
else: 
    if precoFinal > maiorP:
        maiorP = precoFinal
    if precoFinal < menorP:
        menorp = precoFinal

adicional - adicional / 12
print(f"Adicional: {adicional}")
print(f"Maior P: {maiorP}")
print(f"Menor P: {menorP}")
print(f"Tot Imp: {totImp}")
print(f"Quantidade Barato: {qtdB}")
print(f"Quantidade Normal: {qtdN}")
print(f"Quantidade Caro: {qtdC}")