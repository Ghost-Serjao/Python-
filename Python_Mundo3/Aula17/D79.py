num = []
while True:
    n = int(input('Digite um valor:'))
    if n not in num:
        num.append(n)
        print('Número adicionado com sucesso.')
    else:
        print('Número duplicado! Não foi adicionado. ')
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
num.sort()
print(num)



#Usuario pode digitar varios valores num
#cadastre os em uma lista
#caso o num ja exista la ele n sera add
#no final serão exibidos todos os valores unicos digitados em ordem crescente
