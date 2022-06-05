print('Bem vindo ao site \n calcule o preço de sua vigem logo abaixo')
distancia = float(input('Qual a distancia ate o destino(Km): '))
if distancia <= 200:
    valor = 0.5 * distancia
    print(f'O preço da viagem ficara R${valor} ')
else: 
    valor = 0.45 * distancia
    print(f'O preço da viagem ficara R${valor} ')









#pergunte a distancia
#calcule o preço da passagem cobrado por R$0.50 ate 200km
#R$0.45 para viagens acima de 200km