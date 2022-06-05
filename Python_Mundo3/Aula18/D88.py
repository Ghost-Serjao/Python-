from random import randint
lista = list()
jogos = list()
print('MEGA SENA')
quant = int(input('Quantos jogos deseja fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break 
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print(f'Os números sorteados foram:{jogos}')
    







#Ajuda a criar palpites mega sena 
#Perguntar quantos jogos serão gerados
#e vai sortear 6 num entre 1 e 60 cadstrar numa lista composta 
#Não repetir o mesmo numero no mesmo jogo
#Colocar em ordem  
#Usar timer (sleep)