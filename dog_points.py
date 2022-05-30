# N dogs participate in the dog race, each of them has a certain number of points for the season. Each dog's points are displayed on a huge scoreboard. However, a bug was discovered during the withdrawal: the dogs with the highest and lowest scores were swapped! We need to fix this.
# Given a list of points out of N dogs. Write a program that swaps the largest and smallest elements in a list.

dogs_num = int(input('Dogs number: '))
dogs = []

for _ in range(dogs_num):
    dogs.append(int(input('Enter dog points: ')))

max_num, min_num = max(dogs), min(dogs)

for i_dog in range(dogs_num):
    if dogs[i_dog] == max_num:
        dogs[i_dog] = min_num
    elif dogs[i_dog] == min_num:
        dogs[i_dog] = max_num

print(dogs)