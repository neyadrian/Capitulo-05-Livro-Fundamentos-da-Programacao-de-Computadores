#Faça um programa que leia o número de termos e um valor positivo para X. Calcule e mostre o valor da série a seguir:

fim : int 
i : int 
j : int 
x : int 
expoente : int 
numTermos : int 
den : int 
denominador : int 
fat : int 
s : int 

numTermos = int(input("Digite um número termo: "))
s = 0 
denominador = 1

for i in range(1, numTermos):
    fim = denominador
    fat = 1 

for j in range(1, fim):
    fat = fat * j

expoente = i + 1 
if (expoente/2) == 0:
    s = s - x ** expoente / fat
    
else:
    s = s + x ** expoente / fat 

if denominador == 4:
    den = -1 

if denominador == 1:
    den = 1

if den == 1:
    denominador = denominador + 1 

else:
    denominador = denominador - 1

print(f"{s}")