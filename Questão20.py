#Faça um programa para ler o código, o sexo (M — masculino; F — feminino) e o número de horas/
#aula dadas mensalmente pelos professores de uma universidade, sabendo-se que cada hora/aula vale
#R$ 30,00. Emita uma listagem contendo o código, o salário bruto e o salário líquido (levando em
#consideração os descontos explicados a seguir) de todos os professores. Mostre também a média dos
#salários líquidos dos professores do sexo masculino e a média dos salários líquidos dos professores do
#sexo feminino. Considere:
    #■ desconto para homens, 10%, e, para mulheres, 5%;
    #■ as informações terminarão quando for lido o código = 99999.

cod : int 
numH : int 
salB : int 
salL : int 
mediaM : float 
mediaF : float 
contM : int 
contF : int 
sexo : str 

cod = int(input("Digite um código: "))
contM = 0 
contF = 0 

while cod != 99999:
    sexo = input("Digite o sexo (M ou F): ")
    numH = int(input("Digite o número de horas: "))
    salB = numH * 30 
    if sexo == "M":
        salL = salB - (salB * 10 / 100)
        mediaM = mediaM + salL 
        contM = contM + 1 
    if sexo == "F":
        salL = salL - (salB * 5 / 100)
        mediaF = mediaF + salL
        contF = contF + 1 

print(f"Código: {cod}")
print(f"Salário B: {salB}")
print(f"Salário L: {salL}")

if contM == 0:
    print("Nenhum professor do sexo masculino")
else:
    mediaM = mediaM / contM
    print(f"A média de professores do sexo masculino foi {mediaM}")

if contF == 0:
    print("Nenhum professor do sexo feminino")
else:
    mediaF = mediaF / contF
    print(f"A média de professores do sexo feminino foi {mediaF}")