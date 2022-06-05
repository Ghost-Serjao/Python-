n1 = int(input('Digite o °1 valor: '))
n2 = int(input('Digite o °2 valor: '))
opção = 0
while opção != 5:
    print('''    [1]SOMAR 
    [2]MULTIPLICAR 
    [3]MAIOR 
    [4]NOVOS NUMEROS 
    [5]SAIR DO PROGAMA''')
    opção = int(input('DIGITE AQUI: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}. ')
    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}.') 
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é o maior valor.')
        else:
            print(f'{n2} é o maior valor.')  
    elif opção == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Digite o °1 valor: '))
        n2 = int(input('Digite o °2 valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente')         
print('Fim do progama, volte sempre!')
