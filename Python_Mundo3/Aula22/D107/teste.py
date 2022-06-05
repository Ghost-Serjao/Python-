import moeda

print('Aumentar/Diminuir/Dobro/Metada')
n = float(input('Digite o preço R$ '))
print(f'Aumentar 10%:{moeda.aumentar(n, 10)}')
print(f'Diminuir 10%:{moeda.diminuir(n, 10)}')
print(f'Dobro:{moeda.dobro(n)}')
print(f'Metade:{moeda.metade(n)}')
print(n)




