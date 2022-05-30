user_name = input('Enter username: ')
file_name = input('Enter file name: ')

path = 'C:/{user}/docks/folder/{new_file}'.format(user=user_name, new_file=file_name)

if not path.endswith('.txt'):
    print('Error. Incorrect filetype.')
elif not path.startswith('C:/'):
    print('Error. Incorect disk selected')
else:
    print('File path: ', path)