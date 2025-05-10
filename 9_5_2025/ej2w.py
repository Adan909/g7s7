#pedir contraseña hasta que sea correcta

contraseña = "1234"
intentos = 0
while True:
    contrasena = input("Introduce la contraseña: ")
    intentos += 1
    if contrasena == contraseña:
        print("Contraseña correcta")
        break
    elif intentos >= 3:
        print("Demasiados intentos fallidos")
        break
    else:
        print("Contraseña incorrecta")