print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro #mostrar o termo.
cont = 1 #mostrar quantos termos teve.
total = 0
mais = 10 #Vai mostar 10, depois que o usuario pode escolher mais.
while mais != 0:
    total += mais 
    while cont <= total: #enquanto não chegar ate o 10 termo n para.
        print(f'{termo}->', end=' ')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostar a mais ? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')











#melhor o desafio 51
#mostrar o 10 termos 
#ao inves de acabr perguntar quantos termos mais o usuario quer
