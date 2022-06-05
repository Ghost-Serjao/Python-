from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = (float(input('Comprimento do cateto adjacente: ')))
h1 = hypot(co, ca)
print(f'A hipotenusa vai medir {h1:.2f}')

#Forma com importação