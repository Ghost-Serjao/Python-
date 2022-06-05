#Com função
def soma(a, b):                            
    s = a + b
    print(s)

soma(4, 5)

soma(8, 9)
soma(2, 1)

'''#Sem fução
a = 4 
b = 5
s = a + b 
print(s)

a = 8
b = 9
s = a + b 
print(s)

a = 2 
b = 1
s = a + b 
print(s)'''

def contador(* num):
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
#Duvidas voltra a aula 20 min:32

#Função para dobrar valores de uma lista
def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos]*=2
        pos+=1

lista = [1, 2, 3, 4, 5]
dobra(lista)
print(lista)

#Desempacotamento

def soma(* valores):
    s = 0 
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5, 2)
soma(2, 9, 4)
