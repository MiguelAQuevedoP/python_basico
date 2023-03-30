import math


def desicion():
    confirm = input('Deseas regresar al menu\n[Y/N]\n')
    if (confirm == 'Y' or confirm == 'y'):
        run()
    elif(confirm == 'N' or confirm == 'n'):
        print('Saliste del sistema')
        exit()
    else:
        print("invalid answer.\nComing back to menu...")
        run()


def menu(num_select):
    if num_select == 1:
        side_size = int(input('Digite el tamaño del lado: '))
        area = math.pow(side_size, 2)
        print('El area del cuadrado es: ' + str(area))
        desicion()
    elif num_select == 2:
        base_size = int(input('Digite el tamaño de la base: '))
        height_size = int(input('Digite el tamaño de la altura: '))
        area = base_size * height_size
        print('El area del rectangulo es: ' + str(area))
        desicion()
    elif num_select == 3:
        base_size = int(input('Digite el tamaño de la base: '))
        height_size = int(input('Digite el tamaño de la altura: '))
        area = (base_size * height_size)/2
        print('El area del triangulo es: ' + str(area))
        desicion()
    elif num_select == 4:
        num_side = int(input('Digite el numero del lados: '))
        side_size = int(input('Digite el tamaño del lado: '))
        if num_side < 3:
            print('No se puede obtener el area de un poligono de dos lados!')
            desicion()
        else:
            ap = (side_size)/(2 * math.tan((2 * math.pi)/(2*num_side)))
            area = (num_side * side_size * ap)/(2)
            area = round(area, 2)
            print('El area del poligono de ' + str(num_side) 
                  + ' lados y tamaño de los lados ' + str(side_size) + ' es de: ' + str(area))
        desicion()
    elif num_select == 5:
        print('SALISTE DEL SISTEMA\nVuelve pronto')
        exit()


def run():
    num_select = int(input(' M E N U '
          + '\n1. Area de un cuadrado'
          + '\n2. Area de un rectagulo'
          + '\n3. Area de un triangulo'
          + '\n4. Area de un poligono de N caras'
          + '\n5. SALIR DEL SISTEMA'
          + '\n DIGITE EL NUMERO DE LA OPCION QUE DESEA: \n'))
    menu(num_select)


if __name__ == '__main__':
    run()