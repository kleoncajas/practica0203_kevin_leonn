palabra = input("Introduce una palabra  ")
palabra = palabra.lower()
if palabra == palabra[::-1]:
    print("La palabra en un palíndromo")
else:
    print("La palabra no es un palíndromo")