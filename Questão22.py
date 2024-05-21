#Uma empresa decidiu fazer um levantamento em relação aos candidatos que se apresentarem para
#preenchimento de vagas em seu quadro de funcionários. Supondo que você seja o programador dessa
#empresa, faça um programa que leia, para cada candidato, a idade, o sexo (M ou F) e a experiência no
#serviço (S ou N). Para encerrar a entrada de dados, digite zero para a idade.
#O programa também deve calcular e mostrar:
    #■ o número de candidatos do sexo feminino;
    #■ o número de candidatos do sexo masculino;
    #■ a idade média dos homens que já têm experiência no serviço;
    #■ a porcentagem dos homens com mais de 45 anos entre o total dos homens;
    #■ o número de mulheres com idade inferior a 21 anos e com experiência no serviço;
    #■ a menor idade entre as mulheres que já têm experiência no serviço.

idade : int 
totF : int 
totM : int 
soma1 : int 
contM1 : int
contM2 : int
tot : int 
contF1 : int 
mediaIdade : float 
perc : int 
menorIdade : int 
sexo : str 
exp : str 

idade = int(input("Digite a idade: "))

while idade != 0:
    sexo = input("Digite o sexo (F ou M): ")
    exp = input("Tem experiência (S ou N): ")
    if sexo == "F" and exp == "S":
        if tot == 0:
            menorIdade = idade 
            tot = 1
        elif idade < menorIdade:
            menorIdade = idade 
        
    if sexo == "M":
        totM = totM + 1 

    if sexo == "F":
        totF = totF + 1 

    if sexo == "F" and idade < 21 and exp == "S":
        contF1 = contF1 + 1

    if sexo == "M" and idade > 45:
        contM1 = contM1 + 1 

    if sexo == "M" and exp == "S":
        soma1 = soma1 + idade
        contM2 = contM2 + 1 

print(f"Total feminino: {totF}")
print(f"Total masculino: {totM}")

if contM2 == 0:
    print("Nenhum homem com experiência")
else:
    mediaIdade = soma1 / contM2
    print(f"Média de idade: {mediaIdade}")

if totM == 0:
    print("Nenhum homem")
else:
    perc = contM1 * 100 / totM
    print(f"Percentual: {perc}")

print(f"Cont F1: {contF1}")
print(f"Menor idade: {menorIdade}")