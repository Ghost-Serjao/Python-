continuar = 's'
contador = total = mais1000 = menor = maior = 0
barato = ' '
while continuar != 'N':
    contador += 1
    nome = str(input(f'Nome do °{contador} produto: ')).upper().strip()
    preço = float(input('Preço R$ '))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    total += preço
    if preço >= 1000:
        mais1000 += 1
    if contador == 1: #cont == 1 (o primeiro produto) menor = preço (fica sendo o menor preço)
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
print(f'Dentre os {contador} produtos')
print(f'O preço total é de R${total}')
print(f'{mais1000} custam mais de R$1000')
print(f'{barato} é o mais barato')
   
#Ler nome e preço de varios produtos 
#Perguntar se usuario quer continuar
#A total gasto na compra
#B quantos produtos custam mais de 1000 
#C qual é o nome do produto mais barato
