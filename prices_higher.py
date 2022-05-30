def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)

price = [float(input('Staff price: ')) for _ in range(5)]
first_year_rise = float(input('First year rising: '))
second_year_rise = float(input('Second year rising: '))

first_year = [get_higher_price(first_year_rise, i_price) for i_price in price]
second_year = [get_higher_price(second_year_rise, i_price) for i_price in first_year]

print(f'Prices summ for every year: {round(sum(price), 2), round(sum(first_year), 2), round(sum(second_year), 2)}')