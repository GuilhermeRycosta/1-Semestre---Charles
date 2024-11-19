#Atividade concluída por Ryan Guilherme Costa de Moura

valor = float(input('Digite um valor para ser sacado:'))
if valor <= 0 :
    print('Valor inválido. Digite um valor acima de R$00,00!')
else :
    notas100 = valor//100
    print('notas de R$100:',notas100)
    valor = valor - notas100*100
    
    notas50 = valor//50
    print('notas de R$50: ',notas50)
    valor = valor - notas50*50

    notas20 = valor//20
    print('Notas de R$20: ',notas20)
    valor = valor - notas20*20
    
    notas10 = valor//10
    print('Notas de R$10',notas10)
    valor = valor - notas10*10
    
    notas5 = valor//5
    print('Notas de R$05: ',notas5)
    valor = valor - notas5*5

    notas2 = valor//2
    print('notas de R$02',notas2)
    valor = valor - notas2*2

    cent1 = valor//1
    print('Moedas de R$01: ',cent1)
    valor = valor - cent1

    cent50 = valor//0.50
    print('Moedas de 50 centavos: ',cent50)
    valor = valor - cent50*0.5
    
    cent25 = valor//0.25
    print('Moedas de 25 centavos: ',cent25)
    valor = valor - cent25*0.25

    cent20 = valor//0.20
    print('Moedas de 20 centavos: ',cent20)
    valor = valor - cent20*0.2
    
    cent10 = valor//0.10
    print('Moedas de 10 centavos: ',cent10)
    valor = valor - cent10*0.1
    
    cent05 = valor//0.05
    print('Moedas de 05 centavos: ',cent05)
    valor = valor - cent05*0.05

    cent01 = valor//0.01
    print('Moedas de 01 centavo: ',cent01)

    #188.1