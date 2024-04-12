def ContieneSuma(A,n):
    A.sort()
    
    i, j = 0, len(A) - 1
    
    while i < j:
        suma_actual = A[i] + A[j]
        
        if suma_actual == n:
            return True
        elif suma_actual < n:
            i += 1
        else:
            j -= 1
    
    return False


A = [1, 2, 3, 4, 5]
print(ContieneSuma(A, 23))  
