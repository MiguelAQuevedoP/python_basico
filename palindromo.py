def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    invert_word = word[::-1] #invert the word
    if word == invert_word:
        return True
    else:
        return False


def run():
    word = input("write a word: ")
    is_palindrome = palindrome(word)
    if (is_palindrome):
        print("Is a palindorme word")
    else:
        print("Isn't a palindrome word")

if __name__ == '__main__':
    run()