sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    print('DIGITE SOMENTE M OU F ')   
if sexo == 'M':
    print('Sexo masculino')
elif sexo == 'F':
    print('Sexo feminino')


    



       
#Ler o sexo mas so pode ser M/F
#Se o usuario digitar outra coisa repita ate ele digitar M/F
