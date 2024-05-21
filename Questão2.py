#Faça um programa que leia um valor N inteiro e positivo. Calcule e mostre o valor de E, conforme a
#fórmula a seguir:

#E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

n : int 
e : int 
i : int 
j : int 
fat : int 

n = int(input("Digite um número: "))

for i in range(1, n):
    fat = 1
    for j in range(1, i):
        fat = fat * j 
    e = e + 1 / fat 

print(f"Resultado: {e}")