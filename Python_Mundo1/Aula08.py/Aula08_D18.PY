from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja'))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o seno de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo {angulo} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo {angulo} tem o tangente de {tangente:.2f}')