goods = [["apple", 50], ["orange", 190], ["pineapple", 100], ["peach", 200], ["banana", 77]]

print(f'\nCurrent list: {goods}')

fruit_name = input('Enter new fruit name: ')
price = input('Enter new fruit price: ')

goods.append([fruit_name, price])
print(f'\nNew list: {goods}')
new_price_goods = []

for i in goods:
    c = int(i[1])
    c += c * 8 / 100
    i[1] = c
    new_price_goods.append(i)

print(f'\nNew list with higher tax: {new_price_goods}')
