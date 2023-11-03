#Aqui utilizo el código ascii para el abecedario en letras minúsculas
abecedario = [chr(a)for a in range(97, 123)]
abecedario1 = []
for a,letra in enumerate(abecedario, 1):
    if a %3 != 0:
        abecedario1.append(letra)
print(abecedario1)