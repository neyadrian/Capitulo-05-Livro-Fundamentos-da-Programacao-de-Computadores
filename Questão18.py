#Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado,
#seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math

num : int 
quad : int 
cubo : int 
raiz : int 

num = int(input("Digite um número: "))

while num > 0:
    quad = num * num 
    cubo = num * num * num 
    raiz = math.sqrt(num)

print(f"Quadrado: {quad}, Cubo: {cubo}, Raiz: {raiz}")