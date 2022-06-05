num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero : ')))
print(f'Você digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi digitado pela primeira vez na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado')
print('Os numeros pares foram', end='')
for n in num:
    if num % 2 == 0:
        print(n)
        





#Ler 4 valores e colocar em uma tupla
#A quantas vezes apareceu o valor 9
#B em que posição foi digitado o primeiro valor 3
#C quais foram os numeros pares 
#Se buscar valor que n existe ele da erro 

