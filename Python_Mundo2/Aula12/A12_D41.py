ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
if idade <= 9:
    print('Categoria:Mirim')
elif idade >= 10 and idade <= 14:
    print('Categoria:Infantil')
elif idade >= 15 and idade <= 19:
    print('Categoria:Junior')
elif idade == 20:
    print('Categoria:Senior')
elif idade > 20:
    print('Categoria master')








#Confideração nacional de natação
#ler ano de nascimento e mostrar categoria
#ate 9 mirim  
# ate 14 infantil 
# ate 19 junior 
# ate 20 senior 
# acima de 20 master