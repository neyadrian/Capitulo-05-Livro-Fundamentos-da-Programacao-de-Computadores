#Faça um programa que apresente o menu de opções a seguir, permita ao usuário escolher a opção
#desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibilidade
#de opção inválida e não se preocupe com restrições do tipo salário inválido.
#Menu de opções:
    #1. Imposto
    #2. Novo salário
    #3. Classificação
    #4. Finalizar o programa
#Digite a opção desejada.
#Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir.
#Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário usando as regras a seguir.
#Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando esta tabela:

op : int 
sal : float
imp : int 
aum : int 
novoSal : int 

print("MENU DE OPÇÕES")
print("--------------")
print("1 - Imposto")
print("2 - Novo Salário")
print("3 - Classificação")
print("4 - Finalixar o programa")
print("------------------------")
op = int(input("Digite a opção desejada: "))

if op > 4 or op < 1:
    print("Opção inválida")

if op == 1:
    sal = float(input("Digite o salário: "))
    if sal < 500:
        imp = sal * 5 / 100
    if sal >= 500 and sal <= 850:
        imp= sal * 10 / 100 
    if sal > 850:
        imp = sal * 15 / 100
        print(f"Imposto: {imp}")

if op == 2:
    sal = float(input("Digite o salário: "))
    if sal > 1500:
        aum = 25
    if sal >= 750 and sal <= 1500:
        aum = 50
    if sal >= 450 and sal < 750:
        aum = 75
    if sal < 450:
        aum = 100

    novoSal = sal + aum 
    print(f"Novo salário: {novoSal}")

if op == 3:
    sal = float(input("Digite o salário: "))
    if sal <= 700:
        print("Mal Remunerado")
    else:
        print("Bem Remunerado")

exit (op == 4)