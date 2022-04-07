def year_check(a, b):
    print(f'Years from {a} to {b} with three same numbers: ')
    if a > b:
        a, b = b, a
    for year in range(a, b + 1):
        m = str(year)
        if m.count(m[0]) == 3 or m.count(m[1]) == 3:
            print(year)

a = int(input('Input year from: '))
b = int(input('Input year to: '))

year_check(a, b)
