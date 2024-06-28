def busquedaBinaria(lista, x): 
    pivot = len(lista) // 2
    if len(lista) == 1:
        if lista[0] == x:
            return True
        else:
            return False
    if lista[pivot] > x:
        return busquedaBinaria(lista[:pivot], x)
    elif lista[pivot] < x:
        return busquedaBinaria(lista[pivot:], x)
    else:
        if lista[pivot] == x:
            return True
#print(busquedaBinaria([1, 2, 3, 4, 5, 6, 7, 8, 9], 18))
def quickSelect(lista, k):
    if len(lista) == 1:
        return lista[0]
    pivot = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivot]
    mayores = [x for x in lista if x > pivot]
    pivots = [x for x in lista if x == pivot]
    
    if k < len(menores):
        return quickSelect(menores, k)
    elif k < len(menores) + len(pivots):
        return pivot
    else:
        return quickSelect(mayores, k - len(menores) - len(pivots))
        
def busquedaKesimo(lista, k):
    return quickSelect(lista,k)

#print(busquedaKesimo([3, 2, 1, 5, 4, 6, 7, 8, 9], 7))
def subsecuenciaCreciente(numeros):
    
    def conquer(left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        if len(left) == len(right):
            if left[-1] < right[0]:
                return left + right
            else:
                if left[-1] > right[-1]:
                    return right
                else:
                    return left
        else:
            if left[-1] < right[0]:
                return left + right
            elif len(left) > len(right):
                return left
            else:
                return right
    
    def divide_and_conquer(numeros):
        if len(numeros) <= 1:
            return numeros
        
        # Convert single numbers to lists
        for i in range(len(numeros)):
            numeros[i] = [numeros[i]]        
        while len(numeros) > 1:
            new_numeros = []
            for i in range(0, len(numeros), 2):
                if i + 1 < len(numeros):
                    new_numeros.append(conquer(numeros[i], numeros[i+1]))
                else:
                    new_numeros.append(numeros[i])
            numeros = new_numeros
        
        return numeros[0]
    
    return divide_and_conquer(numeros)

#print(subsecuenciaCreciente([5, 1, 2, 3, 100, 20, 17, 8, 19, 21]))

def kElemMediana(S, k):
    if not S or k < 0 or k >= len(S):
        return None
    
    # Find the median
    mediana = quickSelect(S, len(S) // 2)
    
    # Calculate the absolute differences from the median
    diff = [abs(x - mediana) for x in S]
    
    # Find the k-th smallest difference
    kth_diff = quickSelect(diff, k)
    
    # Find the elements with the k closest differences
    closest_k_elements = [x for x in S if abs(x - mediana) <= kth_diff]
    
    # Sort the closest elements to get exactly k elements
    closest_k_elements.sort(key=lambda x: abs(x - mediana))
    
    return closest_k_elements[:k]

# Test
print(kElemMediana([10,3,6,7,9], 3))