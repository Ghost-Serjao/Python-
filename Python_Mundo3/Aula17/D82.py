lista = []
par = []
impar = []
print('Digite quantos números quer logo abaixo:')
while True:
    n = int(input('Digite:'))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)         
    r = str(input('Quer continuar ? [N para sair]')).upper().strip()[0]
    if r == 'N':
        print('Saindo...')
        break
print('Lista completa:')
print(*lista, sep=', ')
print('Números PARES')
print(*par, sep=', ')
print('Números IMPARES: ')
print(*impar, sep=', ')

#Usuario digitar varios num
#Depois disso crie duas listas extras que vão conter apenas pares e impares digitados respectivamente
#no final mostre o conteudo das 3 listas 