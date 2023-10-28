# encodes password
def encode(password):
    decoded = ''
    for num in password:
        decoded += str((int(num) + 3) % 10)
    return decoded


def decode(password):
    return 0


# executes code
if __name__ == '__main__':
    option = -1
    # loops until exit option
    while option != 3:
        # prints menu
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Exit')
        option = int(input('Please enter an option: '))
        # if option is 1 encodes password
        if option == 1:
            password = input('Please enter your password to encode: ')
            password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        # decoding password
        elif option == 2:
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')
            print()
