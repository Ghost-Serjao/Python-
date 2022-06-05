def leiaint(a):
    a = input(a)
    while True:
        if a.isdigit():
            return a 
        else:
            a = input('Erro, digite um número:')

n = leiaint('Digite um número: ')
print(f'Você digitou o numero {n}.')



#Progama função leiaint() 
# que vai funcionar de forma semelhante com a função input 
# so que fazendo a validação para aceitar somente valor númerico 
# Ex: n = leiaint('Digite um n')