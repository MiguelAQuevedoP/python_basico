def prime(number):
    count = 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        elif number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def run():
    number = int(input("type a number: "))
    if (prime(number)):
        print("Is a prime number")
    else:
        print("Is not a prime number")


if __name__ == "__main__":
    run()