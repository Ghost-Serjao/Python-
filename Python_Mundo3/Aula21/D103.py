def ficha(nome='', gol=''):
    if nome =='':
        nome = '<DESCONHECIDO>'
    if not gol.isdigit():
        gol=0
    print(f'O jogador {nome} fez {gol} gols no campeonato.')

nome = input('nome: ').strip().title()
gol = input('Gols: ').strip()
ficha(nome, gol)



#função chamada ficha que receba dois 
# parametros opcionais:Nome e quantos gols o jogador marcou
#Mostrar a ficha mesmo que algum dado não tenha sido informado corretamente