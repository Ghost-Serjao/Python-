cont = 0
from random import randint
while True:
    cont += 1
    n = int(input('Digite um numero: '))
    e = str(input('Par ou impar? '))
    comp = randint(1, 2)
    res = comp + n
    if res % 2 == 0:
        if e == 'par':
           print('Deu par, você ganhou, vamos de novo...')  
           print(f'Eu joguei {comp} e vc {n}')      
        else:
           print('Deu par, você perdeu.')        
           print(f'Eu joguei {comp} e vc {n}')      
           break               
    elif res % 2 == 1:
       if e == 'impar':
           print('Deu impar, você ganhou...') 
           print(f'Eu joguei {comp} e vc {n}')      
       else:
           print('Deu impar, você perdeu.')
           print(f'Eu joguei {comp} e vc {n}')      
           break
cont -= 1
print(f'Você ganhou {cont} vezes ')






#Jogar par ou impar com o computador
#so sera interrompido quando o jogador perder
#Mostrar quantas vezes o jogador venceu

#Pc pensar em um numero
#ver se é par ou impar
#precisa ser difrente do jogador 
#ver resultado 