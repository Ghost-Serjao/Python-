contador = 0
contador2 = 16
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio','São Paulo',
'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 
'Santos','Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 
'Ceará','Vasco', 'Sport', 'América', 
'Vitória', 'Paraná Clube')
print('BRASILEIRÂO 2018')
print('=' * 35)
print('Os cinco primeiros colocados são:')
for cont in range(0, len(times[:5])):
    contador += 1
    print(f'{contador}-{times[cont]}')
print('=' * 35)
print('Os quatro ultimos colocados são:')
for cont in range(16, len(times[:21])):
    contador2 += 1
    print(f'{contador2}-{times[cont]}')
print('=' * 35)
#for cont in range (14, len(times)):
print(f'A chapecoense ficou na °14 posição')
print('=' * 35)
print('Ordem alfabetica:')
print(sorted(times))

#criar um tupla com os 20 primeiros colocados do brasileirão na ordem
#A Mostrar os 5 primeiros
#B Mostrar os ultimos 4
#C Lista com os times em ordem alfabetica
#D em que posiçao esta a chapecoense