class Trie:
    root = None
    
    def print(self):
        if self.root is None:
            print("Trie is empty.")
            return

        def print_node(node, level=0):
            print("  " * level, end="")
            if node.isEndOfWord:
                print(f"{node.key} ({level}) -")
            else:
                print(f"{node.key} ({level})")

            if node.children:
                for child in node.children:
                    print_node(child, level + 1)

        print("Printing Trie:")
        print_node(self.root)



class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def getChildrenKeys(node):
    if node.children is None:
        return None
    keys = []
    for child in node.children:
        keys.append(child.key)
    return keys




#Bug al insertar hola y luego juan, la j aparece 2 veces
def insert(T,element) :
    # element es una palabra
    #

    # Si está vacío, inserto toda la palabra en la root
    if T.root is None:
        T.root = TrieNode()
        current = T.root
        insertR(current, element)
         

    #Si no está vacío
    
    else:
        current = T.root
        firstChar = element[0]

        if current.children is None:
            return "Error: No debería pasar esto."
        
        childrenKeys = getChildrenKeys(current)


        # Caso 1: Hay que insertar en un nuevo child
        if firstChar not in childrenKeys:
            newNode = TrieNode()
            newNode.key = firstChar
            newNode.parent = current
            current.children.append(newNode)
            element = element[1:]
            insertR(newNode, element)

        # Caso 2: Hay que insertar en un child existente

        if firstChar in childrenKeys:
            # Recorrer el arbol todo lo posible

            def recorrerIguales(node, element):
                # Si llego al final de la palabra
                if len(element) == 1 and node.key == element[0]:
                    return node

                # Si no llego al final de la palabra   

                if node.children is None:
                    return node, element
                
                # Si hay más iguales
                childrenKeys = getChildrenKeys(node)

                if element[0] in childrenKeys:

                    index = childrenKeys.index(element[0])
                    node = node.children[index]
                    element = element[1:]

                    childrenKeys = getChildrenKeys(node)
                    if childrenKeys is None:
                        return node, element
                    return recorrerIguales(node, element)
                
                # Si no hay más iguales
                else:

                    return node, element
                
            
            current, element = recorrerIguales(current, element)

            insertR(current, element)


     

def insertR(node, element):

    if len(element) == 0:
        node.isEndOfWord = True
        
        return

    firstChar = element[0]
    element = element[1:]

    if node.children is None:
        node.children = []
        newNode = TrieNode()
        newNode.key = firstChar
        newNode.parent = node
        node.children.append(newNode)


        return insertR(newNode, element)

    if node.children is not None:
        newNode = TrieNode()
        newNode.key = firstChar
        newNode.parent = node
        node.children.append(newNode)

        
        return insertR(newNode, element)



def search(T, element):
    current = T.root
    return searchR(current, element)

def searchR(node, element):
    nodeChildren = getChildrenKeys(node)
    if nodeChildren is None:
        return False
    if element[0] in nodeChildren:
        index = nodeChildren.index(element[0])
        node = node.children[index]
        element = element[1:]
        if len(element) == 0:
            return True
        return searchR(node, element)
    else:
        return False


def delete(T, element):
    current = T.root
    return deleteR(current, element, None, None, None)

    
def deleteR(node, element, lastEnd, lastBif, lastChar):

    nodeChildren = getChildrenKeys(node)
    if nodeChildren is None:
        return False
    if element[0] in nodeChildren:
        index = nodeChildren.index(element[0])
        node = node.children[index]


        element = element[1:]

        
        #Agregar last bif


        if node.isEndOfWord == True and len(element) != 0:
            lastEnd = node
            lastChar = element[0]
        
        if getChildrenKeys(node):
            if len(getChildrenKeys(node)) > 1:
                lastBif = node
                lastChar = element[0]



        if len(element) == 0:
            #Encontramos la ultima letra
            nodeChildren = getChildrenKeys(node)

            #Si sigue teniendo hijos##########################
            if nodeChildren is not None:
                node.isEndOfWord = False
                return True
            
            #Si no tiene más hijos
            if nodeChildren is None:
                if lastEnd:
                    print("lastEnd: ", lastEnd.key)
                    while node != lastEnd:
                        node = node.parent

                    index = getChildrenKeys(node).index(lastChar)
                    print("Index: ", index)
                    node.children.pop(index)

                    return True
                
                if lastBif:
                    print("lastBif: ", lastBif.key)
                    while node != lastBif:
                        node = node.parent
                    
                    print("Debug, Node: ", node.key)
                    print("Debug, lastChar: ", lastChar)

                    index = getChildrenKeys(node).index(lastChar)
                    print("Index: ", index)
                    node.children.pop(index)

                    return True
        
        
        if node is not None and len(element) > 0:
            return deleteR(node, element, lastEnd, lastBif, lastChar)
        else:
            print("gho")
            return False
    else:
        return False
    



def ejercicio4(T, p, n):
    #dado un árbol Trie T, un patrón p (prefijo) y un entero n, escriba todas las palabras del árbol que empiezan por p y sean de longitud n. 

    #Paso 1: recorrer hasta la última letra de p, contador i
    node = T.root
    element = p
    i = 0
    endOfWordsFound = 0


    while True:
        nodeChildren = getChildrenKeys(node)
        if nodeChildren is None:
            break
        if element[0] in nodeChildren:
            index = nodeChildren.index(element[0])
            node = node.children[index]
            i += 1
            element = element[1:]
            if len(element) == 0:
                break
        else: return False

    #Paso 2: Recorrer completo n - i niveles
    n = n + 1

    endOfWordsFound = recorrerHastaN(node, i, n, 0)

    #Paso 3: Devolver cantidad de endOfWord encontrados

    return endOfWordsFound



def recorrerHastaN(node, i, n, endOfWordFound):

    if i <= n:
        i += 1

        if node.isEndOfWord == True:
            # Bug: endOfWordFound es None
            if i == n:
                endOfWordFound += 1

        childrenKeys = getChildrenKeys(node)

        if childrenKeys is not None:

            for j in range((len(childrenKeys))):
                endOfWordFound = recorrerHastaN(node.children[j], i, n, endOfWordFound)

        return endOfWordFound
    else: return endOfWordFound



def autoCompletar(Trie, cadena):
    return autoCompletarR(Trie.root, cadena)

def autoCompletarR(node, element):

    nodeChildren = getChildrenKeys(node)
    if nodeChildren is None:
        return False

    if len(element) == 0:
        return completeR(node, element, False, "")
    if element[0] in nodeChildren:
        index = nodeChildren.index(element[0])
        node = node.children[index]
        element = element[1:]
        return autoCompletarR(node, element)

    else:
        if len(element) > 1:
            return completeR(node, element, False, "")
    
def completeR(node, element, bifurcations, complete):
    if node.isEndOfWord == True:
        complete = complete[1:]
        complete += node.key
        return complete
    
    nodeChildren = getChildrenKeys(node)
    if len(nodeChildren) != 1:
        bifurcations = True
    
    if bifurcations == True:
        return None
    
    else:
        complete += node.key
        element = element[1:]
        return completeR(node.children[0], element, bifurcations, complete)
    

