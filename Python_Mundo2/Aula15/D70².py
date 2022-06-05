cont = total = tot1000 = 0
barato = ' '
while True:
    cont += 1
    produto = str(input(f'Nome do °{cont} produto: '))
    preço = float(input('Preço R$ '))
    total += preço
    if preço >= 1000:
        tot1000 += 1
    if cont == 1 or preço  < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(':-^40'.format('FIM DO PROGAMA'))
print(f'Dentre os {cont} produtos')
print(f'O preço total é de R${total}')
print(f'{tot1000} custam mais de R$1000')
print(f'{menor} é o mais barato')
