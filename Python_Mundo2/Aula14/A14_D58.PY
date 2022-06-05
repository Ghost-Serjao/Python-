tent = 0
jogador = 0
from random import randint
compu = randint(0, 10)
print('Pensei em um numero entre 0 e 10, tente adivinhar.')
while jogador != compu:
    tent += 1
    jogador = int(input('Em que numero eu pensei? '))
    if jogador != compu:  
        print('ERROU! Tente novamente')              
    elif jogador == compu: 
        print('PARABENS VOCÊ ACERTOU.')
print(f'Precisou de {tent} tentativas')
   








#Melhore o desafio 28 
#So que o jogador vai tentar adivinhar ate ele acertar 
#Mostrando no final quantos palpites foram necessarios para acertar 