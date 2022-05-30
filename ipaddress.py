ip_addrress = input('Enter sample ip-address, in sample use construction {num}: ')

ip = []

for i in range(4):
    num = input(f'Enter {i + 1} number: ')

    if int(num) < 0 or int(num) > 255:
        print('Those ip-address is incorrect')
        print('Enter number from 0 to 255.')
        break
    else:
        ip.append(num)

print(ip_addrress.format(num='.'.join(ip)))