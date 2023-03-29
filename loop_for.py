def run():
    num_tabla = int(input("Digita el numero de la tabla que deseas saber: "))
    for i in range (11):
        result = num_tabla * i
        print(str(num_tabla) + " * " + str(i) + " = " + str(result))


if __name__ == '__main__':
    run()