#Uma empresa possui dez funcionários com as seguintes características: código, número de horas trabalhadas
#no mês, turno de trabalho (M — matutino; V — vespertino; ou N — noturno), categoria (O —
#operário; ou G — gerente), valor da hora trabalhada. Sabendo-se que essa empresa deseja informatizar
#sua folha de pagamento, faça um programa que:
    #a) Leia as informações dos funcionários, exceto o valor da hora trabalhada, não permitindo que sejam informados
        #turnos e nem categorias inexistentes. Trabalhe sempre com a digitação de letras maiúsculas.
    #b) Calcule o valor da hora trabalhada, conforme a tabela a seguir. Adote o valor de R$ 450,00 para o salário
        #mínimo.
    #c) Calcule o salário inicial dos funcionários com base no valor da hora trabalhada e no número de horas trabalhadas.
    #d) Calcule o valor do auxílio alimentação recebido pelo funcionário de acordo com seu salário inicial, conforme
        #a tabela a seguir.
    #e) Mostre o código, número de horas trabalhadas, valor da hora trabalhada, salário inicial, auxílio alimentação
        #e salário final (salário inicial + auxílio alimentação).

cont : int
codigo : int 
nht : int 
valor : int
salMin : int
salInicial : int 
aux : int 
salFinal : int 
turno : str
categoria : str

salMin = 450 

for cont in range(1, 10):
    while turno != "M" and turno != "N":
        turno = input("Digite um turno: ")
    while categoria != "G" and categoria != "O":
        categoria = input("Digite a categoria: ")

    if categoria == "G":
        if turno =="N":
            valor = salMin * 18 / 100
        else:
            valor = salMin * 15 / 100
    else: 
        if turno =="N":
            valor = salMin * 13 / 100
        else:
            valor = salMin * 10 / 100

salInicial = nht * valor

if salInicial <= 300:
    aux = salInicial * 20 / 100
elif salInicial < 600:
    aux = salInicial * 15 / 100
else:
    aux = salInicial * 5 / 100

salFinal = salInicial + aux

print(f"Código: {codigo}, NHT: {nht}, Valor: {valor}, Salário Inicial: {salInicial}, Auxílio: {aux}, Salário Final: {salFinal}")