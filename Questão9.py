#Faça um programa que receba duas notas de seis alunos. Calcule e mostre:
    # a média aritmética das duas notas de cada aluno; e
    # a mensagem que está na tabela a seguir:
    # o total de alunos aprovados;
    # o total de alunos de exame;
    # o total de alunos reprovados;
    # a média da classe.

cont : int
n1 : int
n2 : int 
media : float 
ta : int 
te : int 
tr : int 
mediaClasse : float 
totalClasse : int 

totalClasse = 0 

for cont in range(1, 6):
    n1 = int(input("Informe a primeira nota: "))
    n2 = int(input("Informe a segunda nota: "))
    media = (n1 + n2) / 2 
    print(f"A média é: {media}")
    if media <= 3:
        tr = tr + 1 
        print("REPROVADO")
    if media > 3 and media < 7:
        te = te + 1
        print("EXAME")
    if media >= 7:
        ta = ta + 1
        print("APROVADO")

totalClasse = totalClasse + media 

print("tr")
print("te")
print("ta")

mediaClasse = totalClasse / 6

print(f"{mediaClasse}")