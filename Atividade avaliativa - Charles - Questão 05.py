minutos    = int(input('Quantos minutos você deixou o seu carro no estacionamento? '))
horas  = minutos/60

valor = 0
if horas >= 12:
    print('A estadia do seu carro vai ser de R$30,00.')
else:
    if horas  <= 2:
    #até 2 custa 8 por hora (max 16 reais)

        valor = horas * 8
        print('O valor é: {}'.format(valor))
    
    elif horas <= 4 :
            #custa 5 por hora + 16 (max 26 reais)
                valor = horas * 5 + 16
                print('O valor é: {}'.format(valor))
    elif horas >=3 :
        valor = horas * 5 + 16
        print('O valor é: {}'.format(valor))
    elif horas > 4 :
        valoralor = horas * 3 + 26
        print('O valor é: {}'.format(valor))