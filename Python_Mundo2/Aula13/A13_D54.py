from datetime import date
atual = date.today().year 
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input(f'Data de nascimento {pess} pessoa:'))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E tambem tivemos {menor} pessoas menores de idade.')
    




#print(f'{tot}')
#elif idade < 21:
#    c = menor
#   print(f'{menor}')
   # print(f'Destas 7 pessoas, {c} ja atingiram a maior idade.')

    #print(f'Destas 7 pessoas, {c} não atingiram a maior idade.')










#Ler o ano de nasc de 7 pessoas
#mostrar quantas ja atingiram a maior idade (21 anos)
#E quantas não atingiam a maior idade 