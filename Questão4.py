#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
#Foram obtidos os seguintes dados:
    #a) código da cidade;
    #b) número de veículos de passeio;
    #c) número de acidentes de trânsito com vítimas.
#Deseja-se saber:
    #a) qual é o maior e qual é o menor índice de acidentes de trânsito e a que cidades pertencem;
    #b) qual é a média de veículos nas cinco cidades juntas;
    #c) qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cont : int
cod : int
numVei : int
numAcid : int 
maior : int
cidMaior : int 
menor : int 
cidMenor : int 
mediaVei : float 
somaVei : int
mediaAcid : float 
somaAcid : int
contAcid : int 

somaVei = 0 
somaAcid = 0 
contAcid = 0 

for cont in range(1, 5):
    cod = int(input("Informe cod: "))
    numVei = int(input("Digite o número de veículos: "))
    numAcid = int(input("Digite o número de acidentes: "))
    if cont == 1: 
        maior = numAcid
        cidMaior = cod 
        menor = numAcid
        cidMenor = cod 
    else:
        if numAcid > maior:
            maior = numAcid
            cidMaior = cod
        if numAcid < menor:
            menor = numAcid
            cidMenor = cod 
        
somaVei = somaVei + numVei

if numVei < 2000:
    somaAcid = somaAcid + numAcid
    contAcid = contAcid + 1

print(f"{maior}, {cidMaior}")
print(f"{menor}, {cidMenor}")

mediaVei = somaVei/5

print(f"{mediaVei}")

if contAcid == 0:
    print("Não foi digitada nenhuma cidade com menos de 2000 veículos")
else:
     mediaAcid = somaAcid / contAcid
     print(f"{mediaAcid}")
