time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
    partidas.clear()
    cont = 0
    for c in range(0, tot):
        cont += 1
        partidas.append(int(input(f'Quantos gols na °{cont} partida: ')))
    jogador['golsp'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print('Cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não esiste jogador com o código de {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["golsp"]):
            print(f'    NO jogo {i + 1} fez {g} gols.')
    print('-'*40)
print('FIM DO PROGAM, VOLTE SEMPRE!')

#Aprimorar D93 
#Varios jogadores
#incluir sistema de visualizção com detalhes do aproveitamento de cada jogador 