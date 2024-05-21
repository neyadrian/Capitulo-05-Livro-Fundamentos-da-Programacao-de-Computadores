#Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que: 
    #a) Esse funcionário foi contratado em 2005, com salário inicial de R$ 1.000,00.
    #b) Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial. 
    #c) A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior. 
#Faça um programa que determine o salário atual desse funcionário.

#Declaração de Variáveis
anoAtual : int
salario : float
novoSalario : float
percentual : float 

#Entrada de Dados
salario = float(input("Dgite o salário inicial do funcionário em 2005: "))
ano = 2005
anoAtual = int(input("Digite em que ano estamos: "))
percentual = 1.5 / 100

while ano < anoAtual:
    ano += 1
    salario *= 1 + percentual
    percentual *= 2

print(f"O salario em {ano} é de R$ {salario:.2f}")