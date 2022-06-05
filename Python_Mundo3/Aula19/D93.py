jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
cont = 0
for c in range(0, tot):
    cont += 1
    partidas.append(int(input(f'Quantos gols na °{cont} partida: ')))
jogador['golsp'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print(f'{k} : {v}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["golsp"])} partidas.')
for i, v in enumerate(jogador['golsp']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

#Gerenciar aprovetamento de um jogador de futebol
#Ler nome e quantas partidas ele jogou
#quantidade de gols feitos por partida
#gardar num dicionario (aproveitamento lista) incluindo o total de gols feitos no campeonato