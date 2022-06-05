maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o °{p} peso: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor =peso
print(f'O maior peso lido é {maior}Kg')
print(f'O maior peso lido é {menor}Kg')








#Ler o peso de 5 pessoas 
#Mostrar qual foi o maior e o menor peso lido