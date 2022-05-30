nums_list = []
n = int(input('Numbers in list: '))

for _ in range(n):
    num = int(input('Next number: '))
    nums_list.append(num)

divider = int(input('Enter divider: '))

index_summ = 0
for i_nums_list in range(n):
    if nums_list[i_nums_list] % divider == 0:
        index_summ += i_nums_list + 1
        print(f'Number index {nums_list[i_nums_list]}: {i_nums_list + 1}')

if index_summ == 0:
        print('Nothing is divisible by a divisor.')

print(f'Index summ: {index_summ}')