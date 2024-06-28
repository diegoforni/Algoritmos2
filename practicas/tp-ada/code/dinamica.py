def darCambio(Cambio, Monedas):
    cambiosADar = []
    for i in range(Cambio+1):
        cambiosADar.append(i)

    matriz = [] * len(Monedas)
    for i in range(len(Monedas)):
        matriz.append([0] * len(cambiosADar))    

    
    for i in range(len(Monedas)):
        for j in range(len(cambiosADar)):
            if i == 0:
                matriz[0][j] = cambiosADar[j]
            else:
                if j < Monedas[i]:
                    matriz[i][j] = matriz[i - 1][j]
                else:
                    matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - Monedas[i]] + 1)


    return matriz[len(Monedas) - 1][Cambio]

#print(darCambio(6, [1,3,4]))

def ej13(A,k):
    ceroToK = []
    for i in range(k+1):
        ceroToK.append(i)
    matriz = [] * len(A)
    for i in range(len(A)):
        matriz.append([0] * len(ceroToK))

    for i in range(len(A)):
        for j in range(len(ceroToK)):
            if i == 0:
                if j == A[i]:
                    matriz[0][j] = 1
            else:
                if j < A[i]:
                    matriz[i][j] = matriz[i - 1][j]
                else:
                    if A[i] == j:
                        matriz[i][j] = 1
                    else:
                        if j >= A[i]:
                            matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - A[i]])
        
    return matriz[len(A) - 1][len(ceroToK) - 1] == 1



#print(ej13([1,3,4,5], 7))
import copy

def recorridoMin(matriz, punto):
    matrizAux = matriz
    
    # calcular costo minimo
    def recorridoMinAux(matriz, punto, matrizAux):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i == punto[0] and j == punto[1]:
                    matrizAux[i][j] = matriz[i][j]
                    return
                if i == 0 and j == 0:
                    matrizAux[i][j] = matriz[i][j]
                elif i == 0:
                    matrizAux[i][j] = matrizAux[i][j-1] + matriz[i][j]
                elif j == 0:
                    matrizAux[i][j] = matrizAux[i-1][j] + matriz[i][j]
                else:
                    matrizAux[i][j] = min(matrizAux[i-1][j], matrizAux[i][j-1]) + matriz[i][j]
    
    recorridoMinAux(matriz, punto, matrizAux)
    
    # Reconstruir el recorrido
    puntoActual = punto
    recorrido = []
    while puntoActual != [0, 0]:
        recorrido.append(puntoActual)
        i, j = puntoActual
        if i == 0:
            puntoActual = [i, j - 1]
        elif j == 0:
            puntoActual = [i - 1, j]
        else:
            if matrizAux[i-1][j] < matrizAux[i][j-1]:
                puntoActual = [i - 1, j]
            else:
                puntoActual = [i, j - 1]
    recorrido.append([0, 0])
    recorrido = recorrido[::-1]

    for punto in recorrido:
        y, x = punto
        recorrido[recorrido.index(punto)] = [x,y]
        
    
    return recorrido

#print(recorridoMin([[0, 3, 4, 0, 2], [5, 1, 2, 1, 3]], [1, 4]))

def subcadenaComunMasLarga(c1,c2):
    c1, c2 = c2, c1

    matriz = [] * (len(c1) + 1)
    for i in range(len(c1) + 1):
        matriz.append([0] * (len(c2) + 1))

    for i in range(1, len(c1) + 1):
        for j in range(1, len(c2) + 1):
            if c1[i - 1] == c2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + 1
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1])
    
    i = len(c1)
    j = len(c2)
    cadena = ""
    print(matriz)
    while i > 0 and j > 0:
        if matriz[i][j] == matriz[i - 1][j]:
            i -= 1
        elif matriz[i][j] == matriz[i][j - 1]:
            j -= 1
        else:
            cadena = c1[i - 1] + cadena
            i -= 1
            j -= 1
    return cadena

print(subcadenaComunMasLarga("AGGTAB", "GXTXAYB"))