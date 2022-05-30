import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3 = [('Alive' if squad_1[damage] + squad_2[damage] < 100 else 'Died') for damage in range(10)]

print(f'List for squad 3: {squad_3}')