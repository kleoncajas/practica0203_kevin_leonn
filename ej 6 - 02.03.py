asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
suspensas = []
for asignatura in asignaturas:
    nota = float(input(f"Qué nota has sacado en {asignatura}  "))
    if nota < 5:
      suspensas.append(asignatura)
if suspensas:
   print("Debes repetir")
   for asignatura in suspensas:
      asignaturas.remove(asignatura)
      print(asignatura)
else:
   print("No debes repetir")
print(asignaturas)