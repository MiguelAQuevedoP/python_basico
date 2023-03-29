def menu(select):
    if(select == 1):
        word = input("Write a word or phrase:")
        word = word[::-1]
        print(word)
        print("do you want print a list of characters?")
        confirm = input("[Y/N]")
        if (confirm == "Y" or confirm == "y"):
            for character in word:
                print(character)
            run()
        elif(confirm == "N" or confirm == "n"):
            print("You pressed \"" + confirm + "\" coming back to menu...")
            run()
        else:
            print("invalid answer.\nComing back to menu...")
            run()
    elif(select == 2):
        word = input("Write a word or phrase:")
        previus_letter = input("What character do you want to change?")
        after_letter = input("To what character?")
        print("then do you want to change the character \""
              + previus_letter + "\" to \""
              + after_letter + "\" ?")
        confirm = input("[Y/N]")
        if (confirm == "Y" or confirm == "y"):
            word = word.replace(previus_letter,after_letter)
            print(word)
            run()
        elif(confirm == "N" or confirm == "n"):
            print("You wanted no change the word or phrase.\nComing back to menu...")
            run()
        else:
            print("invalid answer.\nComing back to menu...")
            run()
    elif(select == 3):
        word = input("Write a word or phrase:")
        word = word.upper()
        print(word)
        run()
    elif(select == 4):
        word = input("Write a word or phrase:")
        word = word.lower()
        print(word)
        run()
    elif(select == 5):
        word = input("Write a word or phrase:")
        word = word.replace(" ", "")
        print(word)
        run()
    elif(select == 6):
        word = input("Write a word or phrase:")
        print("The word or phrase have " + str(len(word)) + " characters.")
        run()
    elif(select == 7):
        word = input("Write a word or phrase:")
        letter = input("What letter do you want to search")
        i = 0
        for letter_in_word in word:
            if(letter_in_word == letter):
                i += 1
        print("There is a " + str(i) + " letters \"" + letter + "\"")
        run()
    else:
        print("SALIENDO DEL SISTEMA . . .")

def run():
    print(" M E N U "
          + "\n 1. Invert a word or phrase."
          + "\n 2. Change letters of a word ar phrase"
          + "\n 3. Change text to mayus"
          + "\n 4. Change text to lower"
          + "\n 5. Delete spaces of text"
          + "\n 6. Know number of characters of a phrase"
          + "\n 7. Search a letter in a word"
          + "\n Press another number to exit.")
    select = int(input("TYPE THE DESIRED OPTION AND PRESS ENTER"))
    menu(select)
    

if __name__ == '__main__':
    run()