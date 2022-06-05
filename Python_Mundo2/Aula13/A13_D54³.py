from datetime import date
current = date.today().year 
larger = 0
smaller = 0
for people in range(1, 8):
    birth = int(input(f'{people} person birth certificate: '))
    age = current - birth
    if age >= 21:
        larger += 1
    else:
        smaller += 1
print(f'in all shots {larger} people older.')
print(f'an we also had {smaller} underage people.')
