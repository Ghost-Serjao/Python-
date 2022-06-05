from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
else:
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print(f'O ano {ano} è bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')








#Leia um ano qualquer e mostra se é ou não bissexto