asignatura = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for a in range(len(asignatura)):
    nota = input("Qué nota has sacado en " + asignatura[a] + "?  ")
for a in range(len(asignatura)):
    notas.append(nota)
    print("En", asignatura[a], "has sacado", notas[a])