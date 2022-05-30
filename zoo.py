zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(zoo.index('lion') + 1, 'bear')
zoo.remove('elephant')

print(f'Zoo: {zoo}')
print(f'Lion in room #{zoo.index("lion") + 1}')
print(f'Monkey in room #{zoo.index("monkey") + 1}')