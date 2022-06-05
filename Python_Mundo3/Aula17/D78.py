valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(*valores,sep=',') #Para mostrar a lista de uma forma mais bonita
print(f'O maior valor foi o {max(valores)} na posição {valores.index(max(valores))}') #Se o num for repetido so mostra a 1 pos
print(f'O menor valor foi o {min(valores)} na posição {valores.index(min(valores))}')
#Ler 5 valores num e guardar em uma lista
#Qual foi o maior / menor e suas posiçoes na lista


#Calcular o maior e o menor valor numa lista
#num aqui é o Lista la em cima.
'''if c ==0:
    maior = menor = num
else:
    if num[c] > maior:
        maior = num(c) 
    if num[c] < menor:
        menor = num(c)'''

#Ver as posiçoes 
#i = indice v = valor 

'''for i, v in enumerate(num):
    if v == maior:
        print(f'{i}')

for i, v in enumerate(num):
    if v == menor:
        print(f'{i}')'''