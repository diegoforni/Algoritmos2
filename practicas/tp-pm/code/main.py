def reduceLen(String):
    last = ""
    reduced = ""
    for i in range(len(String)):
        if i == 0:
            last = String[i]
            reduced += String[i]
        else:
            if last != String[i]:
                reduced += String[i]
            last = String[i]
    return reduced

#print(reduceLen("aaabbbccc")) # abc
def isContained(String1,String2):

    orderedChars = [char for char in String1]
    for char in String2:
        if char == orderedChars[0]:
            orderedChars.pop(0)
            if len(orderedChars) == 0:
                return True
    return False
       
#print(isContained("abcd","abracadabra")) 

def isPatternContained(String1,P,c):
    pattern = P.split(c)
    i = 0
    while i < len(String1):
        if String1[i:i+len(pattern[0])] == pattern[0]:
            i += len(pattern[0])
            pattern.pop(0)
            if len(pattern) == 0:
                return True
        else:
            i += 1
    return False

#print(isPatternContained("abracadabra","bra#ca#bra","#")) # True

def createTransitionMatrix(P, alphabet):
    matrix = []
    for i in range(len(P) + 1):
        matrix.append([None] * len(alphabet))
    i = 0
    for row in range(len(P)):
        for col in range(len(alphabet)):
            if alphabet[col] == P[i]:
                matrix[row][col] = i + 1
            else:
                if row == 0:
                    matrix[row][col] = 0
        i += 1
    for row in range(len(P) + 1):
        for col in range(len(alphabet)):
            if matrix[row][col] == None:
                aux = P[:row] + alphabet[col]
                k = len(aux) - 1
                if k == 0:
                    matrix[row][col] = 0
                while k > 0:
                    if aux[:k] == aux[-k:]:
                        matrix[row][col] = k 
                        k = 0
                    k -= 1
                if matrix[row][col] is None:
                    matrix[row][col] = 0
    
    return(matrix)


#print(createTransitionMatrix("aabab", "ab"))

def buscarPatron(String1, P, alphabet):
    matrix = createTransitionMatrix(P, alphabet)
    p = 0
    for i in range(len(String1)):
        if String1[i] not in alphabet:
            p = 0
        else:
            p = matrix[p][alphabet.index(String1[i])]
            if p == len(P):
                return True
    return False
#print(buscarPatron("abracadabra", "cadabr", "abrcd")) # True

def createKMPMatrix(P):
    matrix = [0] * len(P)
    
    for i in range(1, len(P)):
        k = matrix[i - 1]
        
        while k > 0 and P[k] != P[i]:
            k = matrix[k - 1]
        
        if P[k] == P[i]:
            k += 1
        
        matrix[i] = k

    return matrix

def KMP(T,P):
    matrix = createKMPMatrix(P)
    k = 0
    for i in range(len(T)):
        while k > 0 and T[i] != P[k]:
            k = matrix[k - 1]
        
        if T[i] == P[k]:
            k += 1
        
        if k == len(P):
            return True
        
    return False

print(KMP("ababaca","aba")) # True
