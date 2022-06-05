salario = float(input('Digite seu salario R$ '))
if salario >= 1250.01:
    ns = salario + (salario * 10) / 100
else:
    ns = salario + ((salario * 15) / 100)
print(f'Seu novo salario è de R${ns:.2f}')
    









#Perguntar salario
#acima de R$1250.00 == 10% de aumento
#Inferiores ou iguais a R$1250 == aumento de 15%