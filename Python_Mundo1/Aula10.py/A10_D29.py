print('-----BEM VINDO-----')
print('-----VERIFICAR MULTAS-----')
velocidade = float(input('INFORME A VELOCIDADE DO CARRO: '))
if velocidade > 80.0:
    multa = (velocidade - 80) * 7.00
    print('Você estava a cima do limete')
    print(f'Valor a pagar R${multa}')
else:
    print('Você estava na velocidade permitida')
print('VOLTE SEMPRE QUE PRECISAR')









#Ler a velocidade de um carro
#Se pasar de 80km/h == multa
#se menor que 80km/h == sem multa
#multa igual R$7.00 por cada km acima do limite