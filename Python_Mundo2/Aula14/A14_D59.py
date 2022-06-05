print('=-=' * 15)
print('            DIGITE DOIS VALORES')
print('=-=' * 15)
n1 = int(input('Digite o °1 valor: '))
n2 = int(input('Digite o °2 valor: '))
print('=-=' * 15)
print(f'O QUE DESEJA FAZER COM {n1} E {n2}?')
print('=-=' * 15)
print('[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NUMEROS \n[5]SAIR DO PROGAMA')
print('=-=' * 15)
r = int(input('DIGITE AQUI: '))
print('=-=' * 15)
if r == 1:
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é {soma}. ') 
    print('=-=' * 15)
elif r == 2:
    mult = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é {mult}.') 
    print('=-=' * 15)
elif r == 3:
     if n1 > n2:
         print(f'{n1} é o maior valor.')
     else:
        print(f'{n2} é o maior valor.')
        print('=-=' * 15)
elif r == 4:
    print('=-=' * 15)
    print('            DIGITE DOIS VALORES')
    print('=-=' * 15)
    n1 = int(input('Digite o °1 valor: '))
    n2 = int(input('Digite o °2 valor: '))
    print('=-=' * 15)
    print(f'O QUE DESEJA FAZER COM {n1} E {n2}?')
    print('=-=' * 15)
    print('[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NUMEROS \n[5]SAIR DO PROGAMA')
    print('=-=' * 15)
    r = int(input('DIGITE AQUI: '))
    print('=-=' * 15)
    if r == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}. ') 
        print('=-=' * 15)
    elif r == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}.') 
        print('=-=' * 15)
    elif r == 3:
        if n1 > n2:
             print(f'{n1} é o maior valor.')
        else:
            print(f'{n2} é o maior valor.')
            print('=-=' * 15)
elif r == 5:
    print('Saindo do progama...')
print('FIM PROGAMA')


#Ler dois valores e mostrar um menu na tela
# 1 SOMAR 
# 2 MULTIPLICAR
# 3 MAIOR (Maior valor entre os 2) 
# 4 NOVOS NUMEROS (usuario add novos numeros ao nves dos que ele tinha add)
# 5 SAIR DO PROGAMA