from calculo import calculo
print('-'*100)
print('     BEM VINDO(A)! A CALCULADORA DE VELOCIDADE MEDIA')
print('-'*100)

print('-'*100)
print('Distancia ↓')

print('Digite "1" para: km/h\nDigite "2" para: m/s ')
medidaS = str(input('Sua opção: '))
while medidaS != '1' and medidaS != '2' or medidaS == '':
    print('OPS! Opção invalida :( Tente Novamente!')
    print('Digite "1" para: km/h\nDigite "2" para: m/s ')
    medidaS = str(input('Sua opção: '))
if medidaS == '1':
    medidaS = 'Km/h'
    tp = 'horas'
elif medidaS == '2':
    tp = 'segundos'
    medidaS = 'm/s'

deltaSI = str(input(f'Digite o inicio da distancia {medidaS} '))
if deltaSI.isnumeric() is False:
    while True:
        print('OPS! Opção invalida :( Tente Novamente!')
        deltaSI = str(input(f'Digite o inicio da distancia {medidaS} '))
        if deltaSI.isnumeric():
            break

deltaSF = str(input(f'Digite o fim da distancia {medidaS} '))
if deltaSF.isnumeric() is False:
    while True:
        print('OPS! Opção invalida :( Tente Novamente!')
        deltaSF = str(input(f'Digite o fim da distancia {medidaS} '))
        if deltaSF.isnumeric():
            break
print('-'*100)

print('Tempo ↓')

deltaTI = str(input(f'Digite o inicio do tempo ({tp}): '))
if deltaTI.isnumeric() is False:
    while True:
        print('OPS! Opção invalida :( Tente Novamente!')
        deltaTI = str(input(f'Digite o inicio do tempo({tp}): '))
        if deltaTI.isnumeric():
            break

deltaTF = str(input(f'Digite o fim do tempo ({tp}): '))
if deltaTF.isnumeric() is False:
    while True:
        print('OPS! Opção invalida :( Tente Novamente!')
        deltaTF = str(input(f'Digite o fim do tempo ({tp}): '))
        if deltaTF.isnumeric():
            break

print('-'*100)
print(calculo.vm(deltaSI, deltaSF, deltaTI, deltaTF, medidaS))
