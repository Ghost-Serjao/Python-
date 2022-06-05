num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar ? [N para sair]')).upper().strip()[0]
    if r == 'N':
        print('Saindo...')
        break
for i, v in enumerate(num):
    if v % 2 == 0: 
        pares.append(v)
    elif v % 2 == 0:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista de Pares é {pares}')
print(f'A lista de impares é {impares}')