#Faça um programa para calcular a área de um triângulo e que não permita a entrada de dados inválidos,
#ou seja, medidas menores ou iguais a 0.

base : float 
altura : float 
area : float 

base = float(input("Infome a base (Maior que 0): "))
altura = float(input("Infome a altura (Maior que 0): "))

area = base * altura / 2 

print(f"A área é: {area}")