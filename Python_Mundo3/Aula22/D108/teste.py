import moeda

print('Aumentar/Diminuir/Dobro/Metada')
n = float(input('Digite o preço R$'))
print(f'Aumentar 10%:{moeda.moeda(n)} é {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Diminuir 10%:{moeda.moeda(n)} é {moeda.moeda(moeda.diminuir(n, 10))} ')
print(f'Dobro:{moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Metade:{moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')




