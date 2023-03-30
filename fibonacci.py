def run():
    amount = int(input("Digite qué cantidad de numeros de la serie Fibonacci desea: "))
    acum = 0
    num_previous = 1
    i = 0
    while i < amount:
        print(acum)
        res = acum + num_previous
        acum = num_previous
        num_previous = res
        i += 1


if __name__ == '__main__':
    run()