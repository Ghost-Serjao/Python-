from random import randint
from time import sleep   
compu = randint(0, 5)
print('-=-' * 20)
print('Pensei em um numero entre 0 e 5, tente adivinhar.')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(2)
if jogador == compu:
    print('PARABENS VOCÊ ACERTOU.')
else: 
    print(f'VOCÊ PERDEU, eu pensei no numero {compu}.')