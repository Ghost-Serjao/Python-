num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o °{c}: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)      
num[0].sort()
num[1].sort()
print(f'Todos os valores PARES {num[0]}')
print(f'Todos os valores PARES {num[1]}')










#Usuario digitar 7 valores num
#cadastrar em uma unica lista 
#Separar valores pares de impares 
#No final mostre em ordem crescente