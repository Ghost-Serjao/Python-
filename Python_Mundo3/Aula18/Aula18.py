'''lista1 = ['Pedro', 25]
lista2 = ['Maria', 19]
lista3 = ['João', 32]'''

'''lista composta:
[['Pedro', 25], ['Maria', 19],  ['João', 32]]
    0       1       0      1        0     1
        0               1              2             '''

'''print('Aula pratica:')
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Precisa colocar o [:] pq senão muda todas as estruturas 
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera) 

galera= [['João' 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera) #Vai mostrar tudo
ou:
print(galera[2][1]) #Vai mostrar 13
ou:
for p in galera: #Vai mostrar cada pessoa em forma de lista 
    print(p)  #Se quiser so o nome PRINT(P[0]) so idade (P[1])
'''
'''galera = list()
dado = list() #Lista secundaria que vai pegar os dados temporariamente 
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:]) #copia do dado
    dado.clear()'''   #verifica e joga os dados para galera apagando os dados de dado toda vez que faz o laço

print('Ver se é maior de 21')
'''
totalmaior = totalmenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1
        
print(f'Temos {totalmaior} maiores e {totalmenor} menores)'''
