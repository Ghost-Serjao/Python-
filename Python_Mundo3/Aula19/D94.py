galera = []
pessoas = {}
soma = media = cont = 0 
while True:  
    pessoas.clear()
    pessoas['pessoa'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('ERRO! por favor digite somente M ou F...')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! digite apenas S ou N...')
    if resp == 'N':
        break
print(f'Ao todo temos {(len(galera))} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:.2f} anos.')
print(f'As Mulheres cadastradas foram: ',end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["pessoa"]} ',end='')
print()
print(f'As pessoas com idade acima da media foram: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["pessoa"]} ',end='')
print()
#Mais detalhado
'''for p in galera:
    if p['idade'] > media:
        print('          ', end=')
        for k, v in p.items():
            print(f'{k} = {v}: ',end='')
print()'''
print('<< ENCERRADO >>')
#Ler nome, sexo e idade de varias pessoas
#guardar os dados de cada um em um dicionario
#todos os dicionarios em uma lista
#A quantas pessoas tem
#B media de idade
#C lista com todas as mulheres
#D uma lista com todos as pessoas com idade acima da media