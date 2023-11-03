matriz_a = [[1, 2, 3],[4,5,6]]
matriz_b = [[-1, 0],[0, 1],[1, 1]]
filas_a = len(matriz_a)
columnas_a = len(matriz_a[0])
filas_b = len(matriz_b)
columnas_b = len(matriz_b[0])
resultado = [[0, 0],[0, 0]]
for a in range(filas_a):
    for b in range(columnas_b):
        for c in range(columnas_a):
            resultado[a][b] += matriz_a[a][c] * matriz_b[c][b]
for d in resultado:
    print(d)