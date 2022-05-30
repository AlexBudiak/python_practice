nums_list = []
n = int(input('Numbers in list: '))

for _ in range(n):
    num = int(input('Next number: '))
    nums_list.append(num)

maximum = num
minimum = num

for i in nums_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print('Maximum number in list:', maximum)
print('Minimum number in list:', minimum)