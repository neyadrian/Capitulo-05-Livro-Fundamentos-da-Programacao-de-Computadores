#Foi feita uma pesquisa para determinar o índice de mortalidade infantil em certo período. Faça um
#programa que:
    #■ leia o número de crianças nascidas no período;
    #■ identifique o sexo (M ou F) e o tempo de vida de cada criança nascida.
#O programa deve calcular e mostrar:
    #■ a percentagem de crianças do sexo feminino mortas no período;
    #■ a percentagem de crianças do sexo masculino mortas no período;
    #■ a percentagem de crianças que viveram 24 meses ou menos no período.

i : int 
numCri : int 
meses : int 
porF : int 
porM : int 
totF : int 
totM : int 
tot24 : int 
por24 : int 
sexo : str 

numCri = int(input("Digite o número de crianças nascidas no período: "))

totM = 0 
totF = 0 
tot24 = 0 

for i in range(1, numCri):
    sexo = input("Digite o sexo da criança: ")
    meses = int(input("Digite o tempo de vida da criança: "))
    if sexo == "M":
        totM = totM + 1
    if sexo == "F":
        totF = totF + 1
    if meses <= 24:
        tot24 = tot24 + 1

if numCri == 0: 
    print("Nenhuma criança digitada!")
else:
    porM = totM * 100 / numCri
    porF = totF * 100 / numCri 
    por24 = tot24 * 100 / numCri
    print(f"Percentual de crianças do sexo feminino mortas: {porF}")
    print(f"Percentual de crianças do sexo masculino mortas: {porM}")
    print(f"Percentual de crianças com 24 meses ou menos mortas no período: {por24}")
