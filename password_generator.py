import random


def pass_generate():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_',
              '?', '!', '[', '{', '(', ')',
                '}', ']', ',', ';', '.', '>',
                  '<', '~', '°', '^', '&', '$', '#', '"']
    characters = MAYUS + MINUS + NUMS + CHARS
    password = []

    for i in range(15):
        random_character = random.choice(characters)#se elige un caracter al azar
        password.append(random_character)

    password = "".join(password)
    return password


def run():
    password = pass_generate()
    print("your new password is: " + password)


if __name__ == "__main__":
    run()