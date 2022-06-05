'''pessoa = ('Crebin', '39', 'M', '99.88')
del(pessoa) #Apagar a tupla
print(pessoa)''' #Pode ter num e letras

'''pessoa = ('Crebin', '39', 'M', '99.88')
print(pessoa)''' #Pode ter num e letras

#===========================================================================================================================

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Vai juntar as tuplas 
print(c.count(5))  #Quantas vezes esta aparecendo o numero 5
print(c.index(8))  #Em que posição esta o numero 8 (Começa do 0)
print(c.index(5, 1)) #Mostra o segundo 5 e ignora o que esta na posição 0 '''


'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Vai juntar as tuplas 
print(len(c)''' #Vai mostar quantos elementos 


'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Vai juntar as tuplas 
print(c)'''

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(sorted(lanche))''' #Mostra a tupla em ordem

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {comida[cont]} na posiçã {cont}') #Mostra a posição dos itens 
print('Comi pra caramba!')'''

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate:
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')'''
#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-3:])'''#Do -3(Suco) ate o final (Pudim)

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2])''' #Do inicio ate o 2 Hamburguer e Suco (ignora o 2 = Pizza)

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:])''' #Da pizza ate o final (Pudim)

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3])'''#Suco e pizza

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])''' #Le de tras para frente com o '-'

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])'''  #Vai mostrar so o suco

#===========================================================================================================================

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
for cont in range(0, len(lanche)): #Vai do 0 ate o final
print(lanche[cont])''' #Vai Escrever o lanche de O a 5

#----------------------------------------------------------------------------------------------------------------------------

'''lanche= ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {comida[cont]}')
print('Comi pra caramba!')'''

#----------------------------------------------------------------------------------------------------------------------------

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!') #Vai mostra bonito ao inves de -> ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#----------------------------------------------------------------------------------------------------------------------------

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))''' #Vai mostrar o numero de elementos que existem na tupla

#----------------------------------------------------------------------------------------------------------------------------

'''lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)'''     #Vai mostrar tudo

#===========================================================================================================================

#Tuplas são imutaveis #So quando o progama ta parado que não