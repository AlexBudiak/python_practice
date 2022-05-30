s1, s2 = input('First message: '), input('Second message: ')
count1 = s1.count('!') + s1.count('?')
count2 = s2.count('!') + s2.count('?')
if count1 > count2:
    print(s1, s2)
elif count2 > count1:
    print(s2, s1)
else:
    print('Oops')