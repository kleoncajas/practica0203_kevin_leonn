loteria = []
for a in range(8):
    loteria.append(int(input("¿Cuáles son los números ganadores de la lotería?  ")))
    loteria.sort()
print("Los números ganadores de menor a mayor son", loteria)