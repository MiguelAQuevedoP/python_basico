import random

def run():
    random_number = random.randint(1, 100)
    typed_number = int(input("Digita un numero del 1 al 100: "))
    while typed_number != random_number:
        if(typed_number < random_number):
            print("Busca un numero más grande")
        else:
            print("Busca un numero más pequeño")    
        typed_number = int(input("Elige otro número: "))
    print("Ganaste!")        

if __name__ == '__main__':
    run()