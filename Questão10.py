#Em um campeonato de futebol existem cinco times e cada um possui onze jogadores. Faça um programa
#que receba a idade, o peso e a altura de cada um dos jogadores, calcule e mostre:
    #■ a quantidade de jogadores com idade inferior a 18 anos;
    #■ a média das idades dos jogadores de cada time;
    #■ a média das alturas de todos os jogadores do campeonato; e
    #■ a porcentagem de jogadores com mais de 80 kg entre todos os jogadores do campeonato.

contTime : int 
contJog : int 
idade : int 
peso : float 
alt : float 
qtde : int 
mediaIdade : int 
mediaAltura : float 
porc : int 
tot80 : int 

qtde = 0
tot80 = 0 

for contTime in range(1, 5):
    mediaIdade = 0
    for contJog in range(1, 11):
        if idade < 18:
            qtde = qtde + 1 
            mediaIdade = mediaIdade + idade
            mediaAltura = mediaAltura + alt 
        if peso > 80:
            tot80 = tot80 + 1

mediaIdade

print(mediaIdade = mediaIdade / 11)

print(qtde)

mediaAltura = mediaAltura / 55

print(mediaAltura)

porc = tot80 * 100 / 55

print(porc)


