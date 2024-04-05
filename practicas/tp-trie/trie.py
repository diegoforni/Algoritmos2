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

def insert(T,element) :
    # element es una palabra

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
            print("Error: No debería pasar esto.")
            return "Error: No debería pasar esto."
        
        childrenKeys = getChildrenKeys(current)

        print("current firstChild:", current.children[0].key)
        print("firstChar", firstChar)
        print("childrenKeys", childrenKeys) 

        # Caso 1: Hay que insertar en un nuevo child
        if firstChar not in childrenKeys:
            newNode = TrieNode()
            newNode.key = firstChar
            newNode.parent = current
            current.children.append(newNode)
            insertR(newNode, element)
            print("ES ESTE")

        # Caso 2: Hay que insertar en un child existente

        if firstChar in childrenKeys:
            # Recorrer el arbol todo lo posible
            print("Recorrer iguales")

            def recorrerIguales(node, element):
                # Si llego al final de la palabra
                #RAAAAARI
                if len(element) == 1 and node.key == element[0]:
                    return node

                # Si no llego al final de la palabra   

                # estoy acá, no debería pasar, está mal, el que lo programó
                if node.children is None:
                    return node, element
                
                # Si hay más iguales
                childrenKeys = getChildrenKeys(node)

                if element[0] in childrenKeys:
                    print("Hay más iguales, estoy recorriend")
                    print(" estoy viendo: ", element[0])
                    index = childrenKeys.index(element[0])
                    node = node.children[index]
                    element = element[1:]

                    childrenKeys = getChildrenKeys(node)
                    if childrenKeys is None:
                        return node, element
                    return recorrerIguales(node, element)
                
                # Si no hay más iguales
                else:
                    print("No hay más iguales")
                    print("current final adentro de recorrer: ", node.key)
                    return node, element
                
            
            current, element = recorrerIguales(current, element)
            print("current final pre insertar: ", current.key)
            print("current esEndOfWord: ", current.isEndOfWord)
            print("estoy insertando: ", element)
            print("estoy en el nodo: ", current.key)
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

test = Trie()
insert(test, "hola")
insert(test, "hostia")
insert(test, "holanda")
insert(test, "horacio")
insert(test, "juan")
insert(test, "joder")


test.print()

