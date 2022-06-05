palavras =('Gato', 'Cachorro', 'Curso', 'Java', 'Capivara', 'Mercado')
for p in palavras:
    print(f'\nNa palvara {p.upper()} temos ', end=' ')
    for letra in p: #Cada palavra é uma 'lista' então pega cada letra separada
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


#Tupla com varias palavras
#mostrar para cada palavra quais são suas vogais 