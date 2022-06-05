from random import choice
lista = [1, 2, 3, 4, 5]
n = (choice((1, 2, 3, 4, 5)))
print('Tente adivinhar qual numero de 1 a 5 o PC pensou:')
n1 = int(input('Digite: '))
if n1 <= n:
    print(f'Você acertou:{n}')
else: 
    print(f'Você errou, a resposta certa é:{n}')
print('-----Fim progama-----')











#Fazer o computador pensar em um numero entre 1 e 5
#usuario tentar adivinhar 
#falar se o usuario acertou ou não
