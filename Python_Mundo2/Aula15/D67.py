while True:
    print('-' * 30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Progama tabuda encerrado, colte sempre!')
print('-' * 30)

'''#mostre a tabuada de varios numeros 1 de cada vez para cada valor digitado pelo usuario
#o progama sera interrompido quando o numero solicitado for negativo'''
