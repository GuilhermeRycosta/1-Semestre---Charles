#Atividade concluída por Ryan Guilherme Costa De Moura

x = int(input('Digite um número entre 0 e 9999: '))
if x<0:
    print('Valor inválido. Digite um número entre 0 e 9999 na próxima vez.')
elif x>9999:
    print('Valor inválido. Digite um número entre 0 e 9999 na próxima vez.')
else :
    m = x//1000
    x = x%1000
    c = x//100
    x = x%100
    d = x//10
    x = x%10
    u = x//1
    x = x%1
    y = m+c+d+u

    #print('m = ',m)
    #print('c = ',c)
    #print('d = ',d)
    #print('u = ',u)

    print('A soma desses algarismos é: {}'.format(y))
