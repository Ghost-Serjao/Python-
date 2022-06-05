def voto(nasc):
    from datetime import date 
    ano = date.today().year
    idade = ano - nasc
    print(f'Voce tem {idade} anos e ', end='')
    while True:
        if idade <= 15:
            print(f'não pode votar com menos de 16 anos.')
        elif idade == 16 or idade == 17:
            print('o seu voto é opcional.')
        elif idade >= 18 and idade <= 65:
            print('o seu voto é obrigatorio.')
        else:
            print('o seu voto é opcional.')
        break
        
nasc = int(input('Ano de nascimento: '))
voto(nasc)


#Função chamada voto() 
#que vai receber como parametro o ano de nascimento de uma pessoa retornando um 
#valorliteral indicado se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições
#-15 não vota, 16/17 opcional, 18 a 65 obrigatorio, 65+ opcional