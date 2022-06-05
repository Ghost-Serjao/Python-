contador = mais18 = homens = mulher20 = 0
continuar = 's'
while continuar != 'N': 
    contador += 1
    print(f'{contador}ª pessoa')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    continuar = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if idade >= 18:
       mais18 += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
print(f'Tem {contador} pessoas:')
print(f'{mais18} com mais de 18 anos')
print(f'{homens} homens')
print(f'{mulher20} mulheres com menos de 20 anos')




#Ler a idade e sexo de varias pessoas
#a cada pessoa o progama deve perguntar se quer ou n continuar
#no final mostre:
#A quantos tem 18+ 
#B Quantos homens 
#C quantas mulheres tem menos de 20 anos