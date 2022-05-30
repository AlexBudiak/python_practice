num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

even_list = [num for num in range(num_1, num_2 + 1) if num % 2 == 0]

print(f'Even numbers from {num_1} to {num_2}: {even_list}')