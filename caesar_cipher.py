def ceaser_code():
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    encrypt = input('Enter message: ')
    key = int(input('Enter shift from 1 to 25: '))
    encrypt = encrypt.lower()
    encrypted = ''

    encrypted = [alphabet[alphabet.find(letter) + key] if letter in alphabet else encrypted + letter for letter in encrypt]
    encrypted_str = ''.join(encrypted)
    return encrypted_str

print(ceaser_code())