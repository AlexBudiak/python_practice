text = input('Enter text: ')

lower, upper = 0, 0
for sym in text:
    if sym.islower():
        lower += 1
    else:
        upper += 1

if lower > upper:
    print(text.lower())
else:
    print(text.upper())