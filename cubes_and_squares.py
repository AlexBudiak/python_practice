a = int(input('Enter left board: '))
b = int(input('Enter right board: '))

cubes = [a * a * a for a in range(a, b + 1)]
squares = [a * a for a in range(a, b + 1)]

print(f'List of cubes from {a} to {b}: {cubes}')
print(f'List of cubes from {a} to {b}: {squares}')