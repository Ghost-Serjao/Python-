from math import factorial 
n = int(input('Digite um numero: '))
factorial(n)
print(n)
if n < 0:
    print('Não existe fatorial de numero negativo')
elif n == 0:
    print('1')
else:
    fact = 1
    while (n > 1):
        fact *= n
        n -= 1
    print(fact)








#Ler um numero e mostrar seu fatorial
#fazer com FOR e WhILE
