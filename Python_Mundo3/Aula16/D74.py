from random import sample #A função sample é melhor nesse caso
numeros = tuple(sample(range(10), 5)) #sortear nuemros de 0 a 10, 5 vezes
print('Os numeros gerados sâo:')
for i in numeros:
    print(i, end=' ')
print(f'''
O maior valor é:{max(numeros)}
O menor valor é:{min(numeros)}
''')












#Gerar 5 numeros aleatorias e colocar em uma tupla
#mostar a listagem dos numeros gerados 
#mostrar o maior e o menor 