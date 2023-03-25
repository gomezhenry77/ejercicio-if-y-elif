primerNumero = int(input("digite primer número"))
segundoNumero = int(input("digite segundo número"))
tecerNumero = int(input("digite tercer número"))
cuartoNumero = int(input("digite cuarto número"))
if (primerNumero == segundoNumero and tecerNumero == cuartoNumero and primerNumero == tecerNumero):
    print("todos los números son iguales")
elif (primerNumero != segundoNumero and tecerNumero != cuartoNumero and primerNumero != tecerNumero):
    print("todos los números son diferentes")
