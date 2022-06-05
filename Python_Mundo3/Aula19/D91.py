from time import sleep
from operator import itemgetter
from random import randint
dic = {}
cont = 0
jogador1 = randint(1, 7)
dic['jogador1'] = jogador1 
jogador2 = randint(1, 7)
dic['jogador2'] = jogador2
jogador3 = randint(1, 7)
dic['jogador3'] = jogador3 
jogador4 = randint(1, 7)
dic['jogador4'] = jogador4
print('Quem tirar o maior número vence!')
print('Ordem dos dados:')
for jogadores, dados in sorted(dic.items()):
    print(f'{jogadores} tirou -> {dados} ')
    sleep(1) 
print('Ranking dos jogadores: ')
for jogadores, dados in sorted(dic.items(),key=itemgetter(1),reverse=True):
    cont += 1
    print(f'{cont} - {jogadores} tirou {dados}')
print('FIM DO PROGAMA')






#Crie um progama onde 4 jogadores jogam um dado (ta entre 1 e 6)
#guardar em um dicionario 
#no final colocar um dicionario em ordem 
#sabendo que o vencedor tirou o maior numero do dado

