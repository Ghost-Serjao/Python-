n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1 #Sempre que for trabalhar com fatorial ou mult e quiser que ela fique limpa, n usar 0 e sim 1
while c > 0:
    print(f'{c} ', end= '')
    print('x ' if c > 1 else ' = ', end= '')
    f *= c
    c -= 1

print(f'{f}')