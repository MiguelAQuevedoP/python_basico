#todas las potencias de 2 hasta 1000
def run():
    i = 0
    LIMIT = 1000000 #is mayus because is a const
    result = 2**i
    while result < LIMIT:
        print("2 ^ " + str(i) + " = " + str(result))
        i = i+1
        result = 2**i


if __name__ == '__main__':
    run()