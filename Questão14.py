#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
#valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

valorInicial : int 
juros : int 
valorParc : int 
total : int 
valorJuros : int 
numParc : int 
i : int 

valorInicial = int(input("Digite o valor inicial da dívida: "))

juros = 0 
numParc = 1
total = valorInicial 
valorParc = valorInicial 

print(f"Total: {total}")
print(f"Juros: {juros}")
print(f"Número da parcela: {numParc}")
print(f"Valor da parcela: {valorParc}")

juros = juros + 10 
numParc = numParc + 2

for i in range(1, 4):
    valorJuros = valorInicial * juros / 100
    total = valorInicial + valorJuros 
    valorParc = total / numParc 
    print(f"Total: {total}")
    print(f"Valor do juros: {valorJuros}")
    print(f"Número da parcela: {numParc}")
    print(f"Valor da parcela: {valorParc}")
    juros = juros + 5 
    numParc = numParc + 3 
    