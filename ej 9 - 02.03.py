palabra = input("Introduce una palabra  ")
palabra = palabra.lower()
vocal1 = 0
vocal2 = 0
vocal3 = 0
vocal4 = 0
vocal5 = 0
letras = ["a", "e", "i", "o", "u"]
for a in range(len(palabra)):
    if palabra [a] == letras[0]:
        vocal1 += 1
print("Hay", vocal1, "letras a")
for e in range(len(palabra)):
    if palabra [e] == letras[1]:
        vocal2 += 1
print("Hay", vocal2, "letras e")
for i in range(len(palabra)):
    if palabra [i] == letras[2]:
        vocal3 += 1
print("Hay", vocal3, "letras i")
for o in range(len(palabra)):
    if palabra [o] == letras[3]:
        vocal4 += 1
print("Hay", vocal4, "letras o")
for u in range(len(palabra)):
    if palabra [u] == letras[4]:
        vocal5 += 1
print("Hay", vocal5, "letras u")