muestra = input("Introduce una muestra de números separados por comas ")
numeros = [float(a)for a in muestra.split(",")]
media = sum(numeros) / len(numeros)
sumatoria = sum((x - media)**2 for x in numeros)
desviacion = (sumatoria / len(numeros))**0.5
print(media)
print(desviacion)