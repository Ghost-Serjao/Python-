from time import sleep #Não usei 

def contador(i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p == 1
        if i < f:
            cont = i
            while cont <= f:
                print(f'{cont} ',end='')
                cont += p
            print('Fim')
        else:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='')
                cont -= p
            print('Fim')
      
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo: ' ))
contador(ini, fim, pas)

#Função chamada contador()
#Receba três parâmetros (inicio, fim e passo)
#Seu progama tem que realizar três contagens
#A) De 1 até 10, de 1 em 1
#B) De 10 até 0, de 2 em 2
#C)Uma contagem personalizada (Uso digitar: Inicio, Fim e passo)
#Funcionar mesmo se o passo for negativo
#Funcionar mesmo se não botar o passo

