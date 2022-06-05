lista = []
print('Digite quantos números quer logo abaixo:')
while True:
    n = int(input('Digite: '))
    lista.append(n)
    r = str(input('Quer continuar ? [N para sair]')).upper().strip()[0]
    if r == 'N':
        print('Saindo...')
        break
print(f'Foram digitados {len(lista)} valores.')
print('Ordenada de forma decrescente: ')
lista.sort(reverse=True)
print(*lista,sep=', ')
if 5 in lista:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')

#uso digitar varios num
#A quantos foram digitados
#B Lista ordenada de forma decrescente
#C se o num 5 foi digitado e esta ou não na lista