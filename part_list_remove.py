import random

n_list = [random.randint(0, n) for n in range(0, int(input('Enter numbers count: ')))]
b = random.randint(0, len(n_list))
a = random.randint(0, b)
print(f'Original list: {n_list}')
print(f'A: {a} \tB: {b}')
del n_list[a:b + 1]
print(f'Corrected list: {n_list}')