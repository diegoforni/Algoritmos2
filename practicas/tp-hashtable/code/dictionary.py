
def hash(k):
    return k % 9

def printDictionary(D):
    for i, bucket in enumerate(D):
        print(f"Bucket {i}: {bucket}")


def insert(D, key, value):
    hashKey = hash(key)

    listToInsert = [key, value]

    if len(D) == 0:
        D = []
        for i in range(9):
            D.insert(i, [])

    if len(D[hashKey]) >= 1:
        bucket = D[hashKey]
        for element in bucket:
            if element[0] == key:
                element[1] = value
                return D

    D[hashKey].append(listToInsert)

    return D  # Return the updated dictionary


def search(D,key):
    hashKey = hash(key)

    bucket = D[hashKey]

    for list in bucket:
        if list[0] == key:
            return list[1]
        

def delete(D, key):
    hashKey = hash(key)
    bucket = D[hashKey]

    i = 0

    for list in bucket:
        if list[0] == key:
            bucket.pop(i)
            return D
        i += 1


def ejercicio4(str1, str2):
    if len(str1) != len(str2):
        return False
    #insertar cada caracter de str1
    dic = []
    for i in range(len(str1)):
        dic = insert(dic, ord(str1[i]), str1[i])


    # eliminar cada caracter de str2 en str1
    for j in range(len(str2)):
        delete(dic, ord(str2[j]))



    for bucket in dic:
        if len(bucket) != 0:
            return False
    return True


def ejercicio5(L):
    dic = []
    i = 0
    for element in L:
        dic = insert(dic, element, element)

    for bucket in dic:
        for list in bucket:
            if list[0] is not None:
                i+=1
    
    return i == len(L)



def hash2(k):
    hashKey = 0
    for i in range(len(k)):
        hashKey = hashKey + (ord(k[i]))*10**i
    return hashKey % 191



def insert2(D, key, value):
    hashKey = hash2(key)

    listToInsert = [key, value]

    if len(D) == 0:
        D = []
        for i in range(191):
            D.insert(i, [])

    if len(D[hashKey]) >= 1:
        bucket = D[hashKey]
        for element in bucket:
            if element[0] == key:
                element[1] = value
                return D

    D[hashKey].append(listToInsert)

    return D  # Return the updated dictionary


def search2(D,key):
    hashKey = hash2(key)

    bucket = D[hashKey]

    for list in bucket:
        if list[0] == key:
            return list[1]
        

def delete2(D, key):
    hashKey = hash2(key)
    bucket = D[hashKey]

    i = 0

    for list in bucket:
        if list[0] == key:
            bucket.pop(i)
            return D
        i += 1



def ejercicio7(string):
    compressedStr = ""
    counter = 1
    last = ""

    for i in range(len(string)):
        char = string[i]
        if i > 0:
            last = string[i-1]
        if char == last:
            counter += 1
            if i == len(string) - 1:
                counter = str(counter)
                compressedStr = compressedStr + counter
                return compressedStr
            if string[i+1] != char:
                counter = str(counter)
                compressedStr = compressedStr + counter
                counter = 1
        else:
            compressedStr = compressedStr + char
       
    return compressedStr

def ejercicio8(S,P):
    hashP = hash2(P)
    lenP = len(P)
    for i in range(len(S)):
        if hash2(S[i:i+lenP]) == hashP:
            return i 
        

def ejercicio9(S,T):
    dictionary = []
    for i in range(len(T)):
        dictionary = insert(dictionary, T[i], T[i])
    for i in range(len(S)):
        searchResult = search(dictionary, S[i])
        if searchResult is None or searchResult != S[i]:
            return False
    return True
        