matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = coluna = seg = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]    
    print()   
print(f'A soma dos valores pares é:{par}.')
for l in range(0, 3):
    coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é:{coluna}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[l][c] > mai:
        mai = matriz[l][c]
print(f'O maior valor da segunda linha é {mai}.')




#Aprimarar d86
#A soma de todos os pares
#B soma da terceira coluna
#C maior valor da segunda linha 