print('=' * 30)
print('BANCO CEV') 
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break



#Simular funcionamento de um caixa eletronico
#Perguntar ususario qual valor a ser sacado (num int)
#Informar quantas cedulas de cada valor serão entregues
#Cedulas: R$50, R$20, R$10 e R$1
 