from random import randint
computador = randint (0, 10)
print('Pensei em um numero entre 0 e 10, tente adivinhar.')
acertou = False
tent = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tent += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...') 
print(f'Acertou com {tent} tentativas, Parabéns')

