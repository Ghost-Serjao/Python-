numeros = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 
'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE',
'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        n = int(input('Digite um numero entre 0 e 20: '))
        if n <= 20 and n >=0:   
            break
        print('Numero fora dos suportados, tente novamente')
    print(f'o número que você digitou é: {numeros[n]}')
    continuar = str(input('Quer continuar? [S/N]:  ')).upper().strip()[0]
    if continuar == 'S':
        print('Continuando...')
    else:
        print('Fim do progama, volte sempre!')
        break

#Ter um tupla que tenha uma contagem por extenso de 0 ate 20
#ler um numero entre 0 e 20 que o usuario digitar e mostar por extenso
#ex: 16 -> 'Voce digitou o numero dezesseis'
#sem usar if so tuplas