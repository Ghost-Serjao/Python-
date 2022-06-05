def maior(* num):
    cont = maior = 0
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ',end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior} ')

maior(1, 2, 3, 4, 5, 6, 7)
maior(10, 15, 5, 7, 1)


#Tenha uma função maior()
#Que reveba varios parametros
#Analisar todos e dizer qual foi o maior valor passado
#Ex:Foram passados x valores e o maior valor foi y
#Se não passar nenhum "Você não passou nenhum valor"
