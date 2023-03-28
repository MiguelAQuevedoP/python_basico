decision = input("Digita 1 para convertir de COP a DOLLAR \nDigita 2 para convertir de DOLLAR a COP \n Luego presiona ENTER.")
decision = int(decision)
if(decision == 1):
    cop = input("¿Cuantos pesos colombianos quieres convertir?: ")
    cop = float(cop)
    dollar_value = 4668.04
    dollar = cop /dollar_value
    dollar = round(dollar, 2) 
    dollar = str(dollar)
    print("Tienes " + dollar + " dolares")
elif(decision == 2):
    dollar = input("¿Cuantos dolares quieres convertir?: ")
    dollar = float(dollar)
    cop_value = 0.00021417365
    cop = dollar /cop_value
    cop = round(cop, 2) 
    cop = str(cop)
    print("Tienes " + cop + " dolares")
else:
    print("Elección no valida \nDigite un valor valido")
