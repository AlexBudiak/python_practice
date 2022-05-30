n = int(input('Number of participant: '))
k = int(input('Number of teams: '))
members = list(range(1, n + 1))
teams = []
num = 1
if n % k == 0:
    for _ in range(n // k):
        teams.append(list(range(num, num + k)))
        num += k
    print(f'Total teams list: {teams}')
else:
    print(f'{n} participants can not be divided for {k} teams')