
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

dictionary = []

dictionary = insert(dictionary, 1, "uno")
dictionary = insert(dictionary, 2, "dos")
dictionary = insert(dictionary, 3, "tres")
dictionary = insert(dictionary, 9, "nueve")
dictionary = insert(dictionary, 18, "18")
dictionary = insert(dictionary, 18, "dieciocho")



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
