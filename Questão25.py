#Faça um programa que receba os dados a seguir de vários produtos: preço unitário, país de origem
#(1 – Estados Unidos; 2 — México; e 3 — outros), meio de transporte (T — terrestre; F — fluvial; e A
#— aéreo), carga perigosa (S — sim; N — não), finalize a entrada de dados com um preço inválido, ou
#seja, menor ou igual a zero. O programa deve calcular e mostrar os itens a seguir.
    #■ O valor do imposto, usando a tabela a seguir.
    #■ O valor do transporte usando a tabela a seguir.
    #■ O valor do seguro, usando a regra a seguir.
#Os produtos que vêm do México e os produtos que utilizam transporte aéreo pagam metade do valor
#do seu preço unitário como seguro.
    #■ O preço final, ou seja, preço unitário mais imposto mais valor do transporte mais valor do seguro.
    #■ O total dos impostos.

preco : float 
imp : int 
transp : int 
seguro : int 
final : int
totalImp : int 
origem : int 
meioT : str 
carga : str

preco = float(input("Digite o preço: "))

while preco > 0:
    origem = int(input("Digite a origem: "))
    meioT = input("Digite o meio t: ")
    carga = input("Digite a carga: ")

    if preco <= 100:
        imp = preco * 5 / 100
    else:
        imp = preco * 10 / 100

    if carga == "S":
        if origem == 1:
            transp = 50
        if origem == 2:
            transp = 21
        if origem == 3:
            transp = 24

    if carga == "N":
        if origem == 1:
            transp = 12
        if origem == 2:
            transp = 21
        if origem == 3:
            transp = 60

    if origem == 2 or meioT == "A":
        seguro = preco / 2
    else:
        seguro = 0

    final = preco + imp + transp + seguro
    totalImp = totalImp + imp 
    print(f"Imposto: {imp}")
    print(f"Transporte: {transp}")
    print(f"Seguro: {seguro}")
    print(f"Final: {final}")

    print(f"Total imposto: {totalImp}")