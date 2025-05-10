vocales = "aeiou"
palabra = (input("Ingrese una palabra: "))


for letra in palabra: 
   if letra.lower() in vocales: 
       print(letra.upper(), end="")
   else:
       print(letra, end="")
