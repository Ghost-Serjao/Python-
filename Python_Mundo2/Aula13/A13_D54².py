from datetime import date
menor = 0 
for c in range(1, 8):
    pessoas = int(input(f'Ano de nascimento da °{c} pessoa: '))
    if date.today().year - pessoas < 21:
        menor += 1
        print(f'\n{7 -menor} São maiores e  {menor} São menores')

#Mais complexo mas de mais dificil entendimeto/manutenção 



