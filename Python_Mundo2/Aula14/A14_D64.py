total = n = soma = res = 0
while n != 999:
    n = int(input('Digite[999 para parar]: '))
    soma += n 
    res = soma - 999    
    total += 1 
total = total - 1
print(f'Foram digitados {total} valores e a soma entre eles é {res}.')
print('FIM')









#ler varios numeros inteiros pelo teclado
#parar so quando digitar o valor 999
#no final mostre quantos numers foram digitados e qual foi a soma entre eles
#desconsiderando flag(999)