while True:
    template = input('Enter wishes template. In template use {name} and {age} construction: ')

    if '{name}' in template and '{age}' in template:
        break
    print('Mistake: one or two construction is absent.')

names_list = input('Enter names separated by commas: ').split(', ')
ages_str = input('Enter age separeted by space: ')
ages = [int(i_num) for i_num in ages_str.split()]

for i_man in range(len(names_list)):
    print(template.format(name=names_list[i_man], age=ages[i_man]))

people = [' '.join([names_list[i_man], str(ages[i_man])]) for i_man in range(len(names_list))]
people_str = ', '.join(people)

print('\nBirthdays: ', people_str)