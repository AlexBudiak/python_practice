pack = []
decode = []
bad_packs = []

packs_amt = int(input('Pachages count: '))

for i_pack_num in range(packs_amt):
    print(f'\nPack number {i_pack_num + 1}')
    for i_bit in range(4):
        print(f'{i_bit + 1} bit: ', end=' ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('A lot of mistakes in pack.')
        bad_packs += 1
    pack = []

print(f'\nRecieved message: {decode}')
print(f'Number of mistakes in message: {decode.count(-1)}')
print(f'Number of lost packs: {bad_packs}')