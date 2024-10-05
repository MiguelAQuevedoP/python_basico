def run ():
    my_dictionary = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }
    #devuelve los dos valores
    for pais, poblacion in my_dictionary.items():
        print(pais + " tiene " + str(poblacion) + " habitantes.")
    #devuelve las llaves
    for pais in my_dictionary.keys():
        print(pais)

    #devuelve el valor
    for pais in my_dictionary.values():
        print(pais)

if __name__ == '__main__':
    run()