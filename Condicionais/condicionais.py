x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('Entrou no if')

if 1 in (x, y, z):
    print('Entrou no if')

# These only test for truthiness:
if x or y or z:
    print('Entrou no if')

if any((x, y, z)):
    print('Entrou no if')