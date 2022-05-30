message = input('Enter message: ')
symbol = input('Enter symbol: ')

double = [w * 2 for w in message]
sym_add = [w + symbol for w in double]

print(f'Doubled list: {double}')
print(f'List with symbol: {sym_add}')