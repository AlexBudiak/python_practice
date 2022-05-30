original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prices = [min_pos if min_pos > 0 else 0 for min_pos in original_prices]

print(new_prices)