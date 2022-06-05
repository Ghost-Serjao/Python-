print('Triangulo')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 > l2 and l3:
    if l2 + l3 > l1:
        print('pode formar um triangulo.')
    else:
        print('Não pode formar um triangulo.')
else:
    if l2 > l1 and l3: 
        if l1 + l3 > l2: 
            print('pode formar um triangulo.')
        else:
            print('Não pode formar um triangulo.')
    else:
        if l3 > l1 and l2:
            if l1 + l2 > l3:
                print('pode formar um triangulo.')
            else:
                print('Não pode formar um triangulo.')
print('FIM PROGAMA')




#Ler o comprimento de 3 retas e dizer se pode ou não formar um triangulo