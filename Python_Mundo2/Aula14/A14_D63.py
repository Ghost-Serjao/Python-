print('Sequencia de fibonacci')
n = int(input('Quantos termos você quer mostar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2 
    t2 = t3 #T1 vira T2, T2 v ira T3.
    cont += 1
print(' -> FIM')








#leia um numero n inteiro qualquer e mostre os n primeiros elementos 
#de um sequencia de fibonacci