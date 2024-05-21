#Faça um programa que leia um número não determinado de pares de valores [m,n], todos inteiros e
#positivos, um par de cada vez, e que calcule e mostre a soma de todos os números inteiros entre m e n
#(inclusive). A digitação de pares terminará quando m for maior ou igual a n.

m : int 
n : int 
soma : int 
i : int 

m = int(input("Digite um número: "))
n = int(input("Digite outro número: "))

while m < n:
    soma = 0
    for i in range(m, n):
        soma = soma + 1
        print(f"O resultado é: {soma}")