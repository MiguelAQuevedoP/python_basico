def run():
    first_word = input('Escriba la primer palabra y presione ENTER: ')
    second_word = input('Escriba la segunda palabra y presione ENTER: ')
    is_anagrama = False

    first_word = first_word.lower()
    first_word = first_word.replace(' ', '')
    second_word = second_word.lower()
    second_word = second_word.replace(' ', '')

    lst_first_word = list(first_word)
    lst_second_word = list(second_word)

    lst_first_word.sort() #sort ordena alfabeticamente el texto
    lst_second_word.sort()

    first_neat = "".join(lst_first_word)
    second_neat = "".join(lst_second_word)

    if first_neat == second_neat:
        is_anagrama = True
        print(is_anagrama)
    else:
        print(is_anagrama)


if __name__ == '__main__':
    run()