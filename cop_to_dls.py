def converter(input_value, coin_value):
    input_value = float(input_value)
    coin_value = coin_value
    out_value = input_value /coin_value
    out_value = round(out_value, 2) 
    out_value = str(out_value)
    return out_value
decision = input("Digita 1 para convertir de COP a DOLLAR \nDigita 2 para convertir de DOLLAR a COP \n Luego presiona ENTER.")
decision = int(decision)
if(decision == 1):
    cop = input("¿Cuantos pesos colombianos quieres convertir?: ")
    dollar_value = 4668.04
    print("Tienes " + converter(cop,dollar_value) + " dolares")
elif(decision == 2):
    dollar = input("¿Cuantos dolares quieres convertir?: ")
    cop_value = 0.00021417365
    print("Tienes " + converter(dollar, cop_value) + " dolares")
else:
    print("Elección no valida \nDigite un valor valido")