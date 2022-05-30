original_prices = [-12, 3, 5, -2, 1]
new_prices = original_prices[:]

for i in range(len(new_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print(f'Мы потеряли: {abs(sum(original_prices) - sum(new_prices))}')