#Faça um programa que receba um número inteiro maior que 1, verifique se o número fornecido é primo
#ou não e mostre uma mensagem de número primo ou de número não primo.
#Um número é primo quando é divisível apenas por 1 e por ele mesmo.

i : int 
num : int 
qtde : int 

num = int(input("Digite um número: "))

for i in range(1, num):
    if (num // 1) == 0:
        qtde = qtde + 1

if qtde > 2:
    print("Número não primo")
    print("Número primo")