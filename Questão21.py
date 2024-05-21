#Faça um programa que receba vários números, calcule e mostre:
    #■ a soma dos números digitados;
    #■ a quantidade de números digitados;
    #■ a média dos números digitados;
    #■ o maior número digitado;
    #■ o menor número digitado;
    #■ a média dos números pares;
    #■ a porcentagem dos números ímpares entre todos os números digitados.
#Finalize a entrada de dados com a digitação do número 30.000.

num : int 
soma : int 
qtd : int 
maior : int 
menor : int 
qtdPar : int 
mediaPar : int 
somaPar : int 
qtdImpar : int 
media : float 
perc : int 

qtd = 0 
qtdPar = 0 
somaPar = 0 
qtdImpar = 0 
soma = 0 

num = int(input("Digite um número: "))

while num != 30000:
    if qtd == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

soma = soma + num
qtd = qtd + 1

if (num // 2) == 0:
    somaPar = somaPar + num 
    qtdPar = qtdPar + 1
else:
    qtdImpar = qtdImpar + 1

if qtd == 0:
    print("Nenhum número digitado")
else:
    print(f"Soma: {soma}")
    print(f"Quantidade: {qtd}")
    media = soma / qtd 
    print(f"Média: {media}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")

    if qtdPar == 0:
        print("Nenhum par")
    else:
        mediaPar = somaPar / qtdPar
        print(f"Média par {mediaPar}")

    perc = qtdImpar * 100 / qtd 
    print(f"O percentual é de {perc}") 