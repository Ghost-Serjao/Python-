soma = cont = 0
while True:
    n = int(input('Digite um numero[999 Para sair]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma entre os {cont} numeros é de {soma}')

#Ler varios numeros int pelo teclado
#So parar quando o usuario digitar 999
#No final mostre quantos num foram digitaos 
#desconsiderar flag