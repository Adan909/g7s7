#sentencia for

suma = 0
expresion = ""
for i in range(1, 11):
    suma += i
    expresion += str(i)
    if i <10:
        expresion += "+"
    print(f"Suma parcial despues de agregar {i}: {suma}")
    
print(f"\nExpresion: {expresion} = {suma}")
