#atividade concluída por Ryan Guilherme
hi         = int(input('Qual a hora da partida?'))
mi         = int(input('Qual o minuto da partida?'))
hf         = int(input('Qual a hora da chegada?'))
mf         = int(input('Qual o minuto da chegada?'))
descanso   = int(input('Quantos segundos você parou de dirigir para descansar?'))
gasosa     = int(input('Quantos litros de combustível você consumiu na viagem?'))
valorGas   = int(input('Qual o valor, em real, do combustível?'))
km         = int(input('Qual a distância percorrida em Km? '))

segundos   = ((hf - hi) * 60 + (mf-mi)) * 60
minutos    = segundos/60
h          = minutos/60
vGlobal    = km/h
vMovimento = km/(((segundos-descanso)/60)/60)
custoGas   =  valorGas * gasosa

kmLitro    = km/gasosa
litroHora  = gasosa/h  
realKm     = valorGas/km

print('Você viajou por {} segundos.'.format(segundos))
print('A velocidade média global foi de {}Km/h e a velocidade media em movimento foi de {}Km/h.'.format(vGlobal, vMovimento))
print('Você gastou R${} em gasolina.'.format(custoGas))
print('O rendimento do combustível foi de {}Km/l, {} l/h e R${} por Km.'.format(kmLitro, litroHora, realKm))
