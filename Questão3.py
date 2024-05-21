#Faça um programa que leia um número N que indica quantos valores inteiros e positivos devem ser
#lidos a seguir. Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial desse valor.

n : int 
num : int 
i : int 
j : int 
fat : int 

n = int(input("Digite um número: "))

for i in range(1, n):
    num = int(input("Digite um número: "))
    fat = 1
    for j in range(1, num):
        fat = fat * j

print(f"Resultado: {fat}")