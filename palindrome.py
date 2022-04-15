def get_input_parameters():
    word = input('Enter word: ')
    return word

def display_result(is_palindrome):
    if is_palindrome:
        print('Word is palindrome')
    else:
        print('Word is not palindrome')

def check_palindrome(word):
    if word == word[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False
    return is_palindrome

if __name__ == '__main__':
    word = get_input_parameters()
    is_palindrome = check_palindrome(word)
    display_result(is_palindrome)
