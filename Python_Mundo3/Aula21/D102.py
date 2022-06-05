def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' x ', end='')
        f *= c
    return f
    
n = int(input('Digite um numero: '))
print(fatorial(n, show=True))




#Progama com função fatorial() que receba dois parametros
# (num a calcular fatorial) 
# e (show que sera um valor logico (opcinal) 
# indicando se mostrado ou não na tela o precesso de calculo de fatorial