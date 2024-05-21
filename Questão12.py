#Em uma fábrica trabalham homens e mulheres divididos em três classes:
    #■ trabalhadores que fazem até 30 peças por mês — classe 1;
    #■ trabalhadores que fazem de 31 a 50 peças por mês — classe 2;
    #■ trabalhadores que fazem mais de 50 peças por mês — classe 3.
#A classe 1 recebe salário mínimo. A classe 2 recebe salário mínimo mais 3% deste salário por peça,
#acima das 30 peças iniciais. A classe 3 recebe salário mínimo mais 5% desse salário por peça, acima das 30
#peças iniciais.
#Faça um programa que receba o número do operário, o número de peças fabricadas no mês, o sexo do
#operário, e que também calcule e mostre:
    #■ o número do operário e seu salário;
    #■ o total da folha de pagamento da fábrica;
    #■ o número total de peças fabricadas no mês;
    #■ a média de peças fabricadas pelos homens;
    #■ a média de peças fabricadas pelas mulheres; e
    #■ o número do operário ou operária de maior salário.
#A fábrica possui 15 operários.

numOp : int 
pecasOp : int 
numMaior : int 
contM : int 
contF : int 
totPecas : int 
cont : int 
mediaM : float 
salarioMaior : int 
mediaF : float 
salarioOp : int 
totFolha : int 
sexoOp : str 

totFolha = 0
totPecas = 0 
mediaM = 0 
mediaF = 0 
contM = 0 
contF = 0 

for cont in range(1, 15):
    numOp = int(input("Digite o número do operário: "))
    sexoOp = input("Digite o sexo do operáro: ")
    pecasOp = int(input("Digite o número de peças pelo operário: "))
    if pecasOp <= 30:
        salarioOp = 450
    if pecasOp > 30 and pecasOp <= 50:
        salarioOp = 450 + ((pecasOp - 30) * 3 / 100 * 450)
    if pecasOp > 50:
        salarioOp = 450 + ((pecasOp - 30) * 5 / 100 * 450)
    print(f"O operário de número {numOp} recebe salário: {salarioOp}")
    totFolha = totFolha + salarioOp
    totPecas = totPecas + pecasOp 
    if sexoOp == "M":
        mediaM = mediaM + pecasOp
        contM = contM + 1 
    else:
        mediaF = mediaF + pecasOp 
        contF = contF + 1 
    if cont == 1:
        salarioMaior = salarioOp
        numMaior = numOp
    else:
        if salarioOp > salarioMaior:
            salarioMaior = salarioOp
            numMaior = numOp

print(f"Total da folha de pagamento: {totFolha}")
print(f"Total de peças fabricadas no mês: {totPecas}")

if contM == 0:
    print("Nenhum homem!")
else:
    mediaM = mediaM / contM 
    print(f"Média de peças fabricadas por homens: {mediaM}")

if contF == 0:
    print("Nenhuma mulher!")
else:
    mediaF = mediaF / contF
    print(f"Média de peças fabricadas por mulheres: {mediaF}")

print(f"Média de peças fabricadas por mulheres: {mediaF}")