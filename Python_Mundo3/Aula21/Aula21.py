#print('''         <<<<<<<<-interactive help->>>>>>>>       ''')
#help(print) #Vai mostrar o que se pode fazer com o comando print()

#print('''         <<<<<<<<-Docstrings->>>>>>>>       ''')
#Se com duvida em oq cada coisa naquela função faz (Seja sua ou de outra pessoa)
#Para mostrar o que a sua função faz so abirar aspas duplas 3 vezes no inicio e no fim logo abaixo do def
'''def contador(i, f, p):  
  """
    manual aqui 

  """     
    c = i
    while c <= f:
        print(f'c', end='..')
        c+=p
    print('FIM')'''

#Contador normal
'''def contador(i, f, p):  
        c = i
        while c <= f:
            print(f'c', end='..')
            c+=p
        print('FIM')

contador(2,10,2)
'''

#print('''         <<<<<<<<-Parametros Opcionais->>>>>>>>       ''')
'''def soma(a, b, c=0): #Caso o C não seja declarado, ele recebera 0 e ficara sendo opcional ao inves de dar erro
    s=a+b+c           #Da para deixar todos como opcionais (a=0, b=0, c=0)
    print(f'A soma vale {s}')
soma(3, 2, 5)
soma(8, 4)'''
#print('''         <<<<<<<<-Escopo de Variáveis->>>>>>>>       ''')
#Local onde a variavel vai existir e onde ela não vai mais existir
#Escopo local so tem valor dentro da função
#Escopo global tem valor dentro e fora da função

#Pode ter variaveis com o mesmo nome e valores diferentes uma em local e outra em local 
#ex
'''def funçao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funçao()
print(f'N1 fora vale {n1}')'''

'''def teste(b):
    global a #usa o A global ou seja o A fora da função vai dexar de ser 5 e valer 8
    a = 8 
    b += 4
    c  = 2 
    print(f'A dentro  vale {a}')
    print(f'B dentro  vale {b}')
    print(f'C dentro  vale {c}')

a = 5 
teste(a) #O valor de A(5) vai virar o valor B(5) dentro da função
print(f'A fora  vale {a}')'''

#print('''         <<<<<<<<-Retorno de Valores->>>>>>>>       ''')
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2}, {r3}. ')
