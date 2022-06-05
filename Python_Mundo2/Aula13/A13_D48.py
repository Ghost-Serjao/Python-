soma = 0
cont = 0
for c in range (1, 501, 2): 
    if c % 3  == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores é {soma}')
      
    








#Soma todos os numeros impares 
#multiplos de 3
#que se encontram entre 1 e 500