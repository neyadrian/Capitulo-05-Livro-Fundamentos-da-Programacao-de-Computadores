#Faça um programa que leia o número de termos, determine e mostre os valores de acordo com a série a seguir:
#Série = 2, 7, 3, 4, 21, 12, 8, 63, 48, 16, 189, 192, 32, 567, 768...

i : int 
numTermos : int 
num1 : int 
num2 : int 
num3 : int 

num1 = 2
num2 = 7
num3 = 3
i = 4

numTermos = int(input("Digite um número termo: "))

print(f"Número 1: {num1}, Número 2: {num2}, Número 3: {num3}")

while i != numTermos:
    num1 = num1 * 2
    print(num1)
    i = i + 1
    if i != numTermos:
        num2 = num2 *3
        print(num2)
        i = i + 1
        if i != numTermos:
            num3 = num3 * 4
            print(num3)
            i = i + 1