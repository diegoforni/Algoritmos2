def darCambioAux(Cambio, Monedas, i, min):
    if Cambio == 0:
        if i < min:
            min = i
        return min
    for moneda in Monedas:
        if Cambio >= moneda:
            min = darCambioAux(Cambio - moneda, Monedas, i + 1, min)
    return min

def darCambio(Cambio, Monedas):
    return darCambioAux(Cambio, Monedas, 0, float('inf'))

#print(darCambio(23, [1,7,9,13,9]))

def mochilaAux(PesoMax, latas, latasUsadas, mayorPesoRegistrado, latasMayorPeso): 
    pesoActual = sum(latasUsadas)
    if pesoActual > mayorPesoRegistrado:
        mayorPesoRegistrado = pesoActual
        latasMayorPeso = latasUsadas
    for lata in latas:
        if pesoActual + lata <= PesoMax:
            mayorPesoRegistrado, latasMayorPeso  = mochilaAux(PesoMax, latas, latasUsadas + [lata] , mayorPesoRegistrado, latasMayorPeso)
    return mayorPesoRegistrado, latasMayorPeso

def mochila(PesoMax, latas):
    return mochilaAux(PesoMax, latas, [], 0, [])[1]

#print(mochila(19, [5, 7, 11, 15]))

def subsecuenciaCreciente(numeros):
    def esCreciente(subsec):
        # Verificar si una subsecuencia es monótona creciente
        return all(subsec[i] < subsec[i + 1] for i in range(len(subsec) - 1))

    def subsecuenciaCrecienteAux(index, current):
        # Si hemos llegado al final del array, verificar si la subsecuencia actual es la más larga encontrada
        if index == len(numeros):
            if esCreciente(current):
                resultados.append(current[:])
            return

        # Opción 1: no incluir el número actual en la subsecuencia
        subsecuenciaCrecienteAux(index + 1, current)

        # Opción 2: incluir el número actual en la subsecuencia
        current.append(numeros[index])
        subsecuenciaCrecienteAux(index + 1, current)
        current.pop()  # Deshacer la inclusión del número actual

    resultados = []
    subsecuenciaCrecienteAux(0, [])
    # Encontrar la subsecuencia más larga entre las subsecuencias crecientes
    return max(resultados, key=len)

# Ejemplo de uso
numeros = [5, 1, 2, 3, 100, 20, 17, 8, 19, 21]
#print(subsecuenciaCreciente(numeros))

def subconjuntoSumaAux(numeros, valor, sumaActual):
    if sumaActual == valor:
        return True
    for n in numeros:
        if sumaActual + n <= valor:
            numeros.remove(n)
            if subconjuntoSumaAux(numeros, valor, sumaActual + n):
                return True
            numeros.append(n)

def subconjuntoSuma(numeros, valor): 
    result = subconjuntoSumaAux(numeros, valor, 0)
    if result:
        return True
    else:
        return False
print(subconjuntoSuma([11, 6, 5, 1, 7, 13, 12], 15))