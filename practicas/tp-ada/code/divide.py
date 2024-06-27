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

def busquedaKesimo(lista, k):
    def quickSelect(lista):
        if len(lista) <= 1:
            return lista
        else:
            pivot = lista[0]
            mayores = []
            menores = []
            for i in range(1, len(lista)):
                if lista[i] < pivot:
                    menores.append(lista[i])
                elif lista[i] > pivot:
                    mayores.append(lista[i])
            if pivot > k:
                return quickSelect(menores)
            elif pivot < k:
                return quickSelect(mayores)
            else:
                return pivot
        
    return quickSelect(lista)

#print(busquedaKesimo([3, 2, 1, 5, 4, 6, 7, 8, 9], 8))
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

print(subsecuenciaCreciente([5, 1, 2, 3, 100, 20, 17, 8, 19, 21]))