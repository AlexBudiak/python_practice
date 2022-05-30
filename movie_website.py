def is_film_exist(movie, film_list):
    for i_movie in film_list:
        if i_movie == movie:
            return True
    return False

films = ['Titanic', 'Home alone', 'Taxi', 'Leon', 'Bohemian rhapsody', 'Sin city', 'Memento', 'Sinners', 'Village', 'Island of treasures', 'Beginning', 'Matrix']

my_list = []

while True:
    print('\nYour current top list', my_list)
    new_movie = input('Film name: ')
    if is_film_exist(new_movie, films):
        print('Commands; add, delete, insert')
        command = input('Enter command: ')
        if command == 'add':
            my_list.append(new_movie)
        if command == 'delete':
            if is_film_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('We have not such film in our list.')
        if command == 'insert':
            index = int(input('Enter position in list: '))
            my_list.insert(index - 1, new_movie)
    else:
        print('No such filf on our website')