print('-=' * 15)
print('NUMERO PRIMO')
print('-=' * 15)
num = int(input('Digite um numero: '))
tot = 0 #se o numero for divisivel é mais um numero no total
for c in range (1, num +1): #Numero + 1 ex:Escolho 7, o python vai ate 6 então add +1
   if num % c == 0: 
    print(f'{c}', end=' ')
    tot += 1 #tot = tot + 1: Se for divisivel TOT (0) acrescenta +1 ou seja, %2 = (TOT + 1, TOT +1) = 2
if tot == 2:
  print(f'\nO numero {num} foi divisivel {tot} vezes')
  print('E por isso ele é primo!')
else:
    print(f'O numero {num} foi divisivel {tot} vezes')
    print('E por isso ele não é primo!')
print('-=' * 15)
print('FIM')
print('-=' * 15)




#Ler um numero inteiro 
#Diga se ele é ou não um numero primo