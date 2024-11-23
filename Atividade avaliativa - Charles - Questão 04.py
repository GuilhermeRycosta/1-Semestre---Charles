dia1 = int(input("Digite o dia inicial: "))
mes1 = int(input("Digite o mês inicial: "))
dia2 = int(input("Digite o dia final: "))
mes2 = int(input("Digite o mês final: "))

#Não sei se faz muita diferença, mas peguei o calendario de 2025 por 2024 ser bissexto.
jan = 31
fev = 28
mar = 31
abr = 30
mai = 31
jun = 30
jul = 31
ago = 31
set = 30
out = 31
nov = 30
dez = 31


dia0 = 0
if mes1 > 1:
    if mes1 > 2:
        dia0 += jan
    if mes1 > 3:
        dia0 += fev
    if mes1 > 4:
        dia0 += mar
    if mes1 > 5:
        dia0 += abr
    if mes1 > 6:
        dia0 += mai
    if mes1 > 7:
        dia0 += jun
    if mes1 > 8:
        dia0 += jul
    if mes1 > 9:
        dia0 += ago
    if mes1 > 10:
        dia0 += set
    if mes1 > 11:
        dia0 += out
    if mes1 > 12:
        dia0 += nov

dia0 += dia1


diaFinal = 0
if mes2 > 1:
    if mes2 > 2:
        diaFinal += jan
    if mes2 > 3:
        diaFinal += fev
    if mes2 > 4:
        diaFinal += mar
    if mes2 > 5:
        diaFinal += abr
    if mes2 > 6:
        diaFinal += mai
    if mes2 > 7:
        diaFinal += jun
    if mes2 > 8:
        diaFinal += jul
    if mes2 > 9:
        diaFinal += ago
    if mes2 > 10:
        diaFinal += set
    if mes2 > 11:
        diaFinal += out
    if mes2 > 12:
        diaFinal += nov

diaFinal += dia2
dias = diaFinal - dia0
if mes1 > mes2:
    print('data invalida')

print('Passaram-se {} dias entre as datas.'.format(dias))