#Diego Forni | Legajo:14329 | mail: d.forni0204@gmail.com

from linkedlist import LinkedList, Node, insert, length, search, add, update


def printList(L):
  current = L.head
  while current is not None:
    print(current.value)
    current = current.nextNode


class BinaryTree:
    root = None

class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None

B = BinaryTree()

#######################################################################
def insertR(newNode, currentNode):
    if newNode.key == currentNode.key:
      return None
    if newNode.key > currentNode.key:
        if currentNode.rightnode is None:
            currentNode.rightnode = newNode
            newNode.parent = currentNode
        else:
            insertR(newNode, currentNode.rightnode)
    else:
        if currentNode.leftnode is None:
            currentNode.leftnode = newNode
            newNode.parent = currentNode
        else:
            insertR(newNode, currentNode.leftnode)

def insert(B, element, key):
    nodeToInsert = BinaryTreeNode()
    nodeToInsert.value = element
    nodeToInsert.key = key
    
    if B.root is None:
        B.root = nodeToInsert
        return key
    else:
        insert = insertR(nodeToInsert, B.root)
        if insert is not None:
          return nodeToInsert.key





#######################################################################
def printBTK(node, indent=""):
  if node is not None:
      print(indent + str(node.key) + ',' + str(node.value))
      if node.leftnode is not None or node.rightnode is not None:
          new_indent = "   " + indent
          if node.leftnode is not None:
              print(new_indent + "L:")
              printBTK(node.leftnode, new_indent)
          if node.rightnode is not None:
              print(new_indent + "R:")
              printBTK(node.rightnode, new_indent)

print("B: ")
printBTK(B.root)
print("")


#######################################################################
def searchR(element, currentNode):

  if currentNode is None:
    return None

  if currentNode.value == element:
    return currentNode.key

  else:
    if currentNode.leftnode is not None:
      resultR = searchR(element, currentNode.leftnode)
      if resultR is not None:
        return resultR
    if currentNode.rightnode is not None:
      resultL = searchR(element, currentNode.rightnode)
      if resultL is not None:
        return resultL

def search(B,element):
  current = B.root
  return(searchR(element, current))
  #Descripción: Busca un elemento en el TAD árbol binario.
  #Entrada: el árbol binario B en el cual se quiere realizar la búsqueda
  #(BinaryTree) y el valor del elemento (element) a buscar.
  #Salida: Devuelve la key asociada a la primera instancia del elemento.
  #Devuelve None si el elemento no se encuentra

##################################################################

def deleteKeyR(current, key, deleted_status):
    if current is None:
        return None
    if key is None:
      return None

    if key < current.key:
        current.leftnode = deleteKeyR(current.leftnode, key, deleted_status)
    elif key > current.key:
        current.rightnode = deleteKeyR(current.rightnode, key, deleted_status)
    else:
        # Node to delete found
        if current.leftnode is None:
            deleted_status[0] = True
            return current.rightnode
        elif current.rightnode is None:
            deleted_status[0] = True
            return current.leftnode

        # Node has two children, find the inorder successor (min of right subtree)
        
        min_right = findMin(current.rightnode)
        leftSub = current.leftnode
        nodeDeleted = deleteKeyR(current, min_right.key, deleted_status)
        rightSub = current.rightnode
        current = min_right
        current.leftnode = leftSub
        current.rightnode = rightSub
        deleted_status[0] = True

    return current


def deleteKey(B, key):
    deleted_status = [False]
    result = deleteKeyR(B.root, key, deleted_status)
    if deleted_status[0]:
        return key
    else:
        return None


def findMin(node):
    while node.leftnode is not None:
        node = node.leftnode
    return node


  




################################################################



def delete(B,element):
  keyToDelete = search(B, element)
  return(deleteKey(B, keyToDelete))
        

#########

def accessR(currentNode, key):
  if currentNode is None:
      return None

  if currentNode.key == key:
      return currentNode.value

  if key > currentNode.key:
      return accessR(currentNode.rightnode, key)  

  if key < currentNode.key:
      return accessR(currentNode.leftnode, key) 

def access(B, key):
  return accessR(B.root, key)



##################################################################
def updateR(currentNode, element, key):
  if currentNode is None:
    return None

  if currentNode.key == key:
    currentNode.value = element
    return currentNode.key

  else:
    if key > currentNode.key:
      updateR(currentNode.rightnode, element, key)
    if key < currentNode.key:
      updateR(currentNode.leftnode,element, key)



    if currentNode.leftnode is not None:
      resultR = searchR(currentNode.leftnode, key)
      if resultR is not None:
        return resultR
    if currentNode.rightnode is not None:
      resultL = searchR(currentNode.rightnode, key)
      if resultL is not None:
        return(resultL)

def update(B, element, key):
  return(updateR(B.root, element, key))




#########delete


################EJERCICIO 2

def reverseList(L):
  prev = None
  current =L.head
  next= L.head


  while current is not None:

    if current.nextNode is None:
      current.nextNode = prev
      L.head = current
      return

    next = next.nextNode
    current.nextNode = prev
    prev = current
    current = next


def traverseInOrderR(current, L):
  if current is not None:
    traverseInOrderR(current.leftnode, L)
    add (L, current.key)
    traverseInOrderR(current.rightnode, L)


def traverseInOrder(B):
  L = LinkedList()
  traverseInOrderR(B.root, L)
  reverseList(L)
  return L

def traverseInPostOrderR(current, L):
  if current is not None:
    traverseInPostOrderR(current.leftnode, L)
    traverseInPostOrderR(current.rightnode, L)
    add (L, current.key)



def traverseInPostOrder(B):
  L = LinkedList()
  traverseInPostOrderR(B.root, L)
  reverseList(L)
  return L

##########

def traverseInPreOrderR(current, L):
  if current is not None:
    add (L, current.key)
    traverseInPreOrderR(current.leftnode, L)
    traverseInPreOrderR(current.rightnode, L)




def traverseInPreOrder(B):
  L = LinkedList()
  traverseInPreOrderR(B.root, L)
  reverseList(L)
  return L

###

def traverseBreadFirstR(current ,L):
  if current is not None:
    if current.leftnode is not None:
      add(L, current.leftnode.key)
    if current.rightnode is not None:
      add(L, current.rightnode.key)
    if current.leftnode is None and current.rightnode is None:
      return
    traverseBreadFirstR(current.leftnode, L)
    traverseBreadFirstR(current.rightnode, L)


def traverseBreadFirst(B):
  L = LinkedList()
  add (L, B.root.key)
  traverseBreadFirstR(B.root, L)
  reverseList(L)
  return L



