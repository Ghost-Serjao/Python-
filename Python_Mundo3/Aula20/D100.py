from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)


#Façã um progama que tenha uma lista chamada numeros[]
#E duas funçoes chmada sorteia() e somapar()
#Sortear 5 numeros e colocar na lista 
#Mostrar a soma entre todos os valores pares mostrada pela função sorteia()
