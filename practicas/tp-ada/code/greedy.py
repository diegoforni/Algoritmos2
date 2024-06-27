def adminActividades(tareas, inicio, fin):
    # ordenar tareas por hora de finalizacion
    tareas.sort(key=lambda x: x[1])
    cronograma = []
    for tarea in tareas:
        if tarea[0] >= inicio and tarea[1] <= fin:
            cronograma.append(tarea)
            inicio = tarea[1]
    return cronograma

#print(adminActividades([[6,7],[8,9],[8,11],[10,11],[11,13],[13,14],[11,12],[12,13]],8,14))

def buscaPares(vector): 
    vector.sort()
    maxSum = 0
    limit = len(vector) // 2
    j = len(vector) 
    for i in range(limit):
        sumaPar = vector[i] + vector[j - 1]
        j -= 1
        if sumaPar > maxSum:
            maxSum = sumaPar
    return maxSum
#print(buscaPares([1, 4, 5, 7, 8,9]))

def mochila(PesoMax, latas): 
    # Sort cans by benefit-to-weight ratio in descending order
    latas.sort(key=lambda x: x[1] / x[0], reverse=True)
    pesoActual = 0
    latasUsadas = []
    
    for lata in latas:
        if pesoActual + lata[0] <= PesoMax:
            pesoActual += lata[0]
            latasUsadas.append(lata)
            
    return latasUsadas

#print(mochila(10, [(2, 3), (3, 4), (4, 8), (5, 8)]))  

def subsecuenciaCreciente(numeros):
    def conquer(left, right):
        print("conquer:", left, right)
        if len(left) == len(right):
            if left[-1] < right[0]:
                print("return:", left + right)
                return left + right
            else:
                if left[-1] > right[-1]:
                    print("return:", left)
                    return right
                else:
                    print("return:", right)
                    return left
        else:
            if left[-1] < right[0]:
                print("return:", left + right)
                return left + right
            elif len(left) > len(right):
                print("return:", left)
                return left
            else:
                print("return:", right)
                return right

    def divide_and_conquer(numeros):
        if len(numeros) <= 1:
            return numeros
        mid = len(numeros) // 2
        left = divide_and_conquer(numeros[:mid])
        right = divide_and_conquer(numeros[mid:])
        return conquer(left, right)

    return divide_and_conquer(numeros)

print(subsecuenciaCreciente([5, 1, 2, 3, 100, 20, 17, 8, 19, 21]))
