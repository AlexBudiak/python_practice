words_list = [input(f'Enter {i + 1} word: ') for i in range(3)]
counts = [0, 0, 0]

text = input('Enter text: ').split(' ')

for word in words_list:
    if word in text:
        counts[words_list.index(word)] += 1

info_list = [' '.join([words_list[i], str(counts[i])]) for i in range(len(words_list))]

print('\nWord count')
for i in range(3):
    print(words_list[i], ':', counts[i])