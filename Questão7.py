#Faça um programa que monte os oito primeiros termos da sequência de Fibonacci.

cont : int 
num1 : int 
num2 : int 
res : int 

num1 = 0
num2 = 1

print(f"Número 1 : {num1}, Número 2: {num2}")

for cont in range(3, 8):
    res = num1 + num2
    print(res)
    num1 = num2 
    num2 = num1
