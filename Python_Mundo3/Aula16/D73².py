times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio','São Paulo',
'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 
'Santos','Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 
'Ceará','Vasco', 'Sport', 'América', 
'Vitória', 'Paraná Clube')
print('BRASILEIRÂO 2018')
print('=' * 35)
for t in times:
    print(t)
print('=' * 35)
print(f'Os cinco primeiros são:{times[0:5]}')
print('=' * 35)
print(f'Os quatro ultimos colocados são:{times[-4:]}')
print('=' * 35)
print(f'Times em ordem alfabetica:{sorted(times)}')
print('=' * 35)
print(f'O chapecoense está na {times.index("Chapeconese")+1}ª posição') #Usar aspas duplas nesses casos
#d += 1
#if c = 'chapecoense':
    #break
#print('O chapecoense está na {d}ª posição)





