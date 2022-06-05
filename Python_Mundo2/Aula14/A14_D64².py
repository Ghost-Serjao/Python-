num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')

#ler o flag do lado de dentro e fora do while pq se o numero for = a 999 ele sai direto sem somar o 999