from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade =  atual - nasc
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    faltam = 18 - idade
    print(f'Ainda faltam {faltam} anos para o alistamento')
    
elif idade > 18:
    passou = idade - 18
    print(f'Você deveria ter se alistado a {passou} anos.')












#ler o ano de nascimento e infromar de acordo com sua idade se vai precisar se alistar
#se ele ainda vai se alistar -18
#ta na hora de se alisatr 18
#ja passou do tempo de alistar 19+
#Falar quanto tempo falta ou quanto tempo passou