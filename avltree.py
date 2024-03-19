class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

# normal bt
    
#Diego Forni | Legajo:14329 | mail: d.forni0204@gmail.com

from linkedlist import LinkedList, Node, insert, length, search, add, update


def printList(L):
  current = L.head
  while current is not None:
    print(current.value)
    current = current.nextNode



B = AVLTree()

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
    nodeToInsert = AVLNode()
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



#######################################################################
def printTBF(node, indent=""):
  if node is not None:
      print(indent + str(node.key) + ',' + str(node.bf))
      if node.leftnode is not None or node.rightnode is not None:
          new_indent = "   " + indent
          if node.leftnode is not None:
              print(new_indent + "L:")
              printTBF(node.leftnode, new_indent)
          if node.rightnode is not None:
              print(new_indent + "R:")
              printTBF(node.rightnode, new_indent)

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

########## Algo 2 TP 2 Ej 1

def rotateRight(Tree,avlnode):
  newRoot = avlnode.leftnode 

  avlnode.leftnode = newRoot.rightnode ## el hijo izquierdo de el avl pasa a ser hijo derecho de la new root

  if newRoot.rightnode is not None:       ## le actualiza el padre al hijo derecho
    newRoot.rightnode.parent = avlnode

  newRoot.parent = avlnode.parent  ### actualizar padre

  if avlnode.parent is None: ## si avl era la raíz, actualizar
    Tree.root = newRoot
  else:                       ## actualiza si nuestro nodo inicial era hijo izquierdo o derecho
    if avlnode.parent.rightnode == avlnode:
      avlnode.parent.rightnode = newRoot
    else:
       avlnode.parent.leftnode = newRoot
  newRoot.rightnode = avlnode ## avl hijo derecho de new root
  avlnode.parent = newRoot ## asignar padre a avl



  return newRoot

def rotateLeft(Tree,avlnode):
  newRoot = avlnode.rightnode
  avlnode.rightnode = newRoot.leftnode

  if newRoot.leftnode is not None:
    newRoot.leftnode.parent = avlnode
  
  newRoot.parent = avlnode.parent

  if avlnode.parent is None:
    Tree.root = newRoot
  else:
      if avlnode.parent.leftnode == avlnode:
        avlnode.parent.leftnode = newRoot
      else:
        avlnode.parent.rightnode = newRoot

  newRoot.leftnode =  avlnode
  avlnode.parent = newRoot
   
  return newRoot


def calculateHeight(node, actualHeight, maxHeight):

  if node.leftnode is None and node.rightnode is None:
    if actualHeight >= maxHeight:
      maxHeight = actualHeight
      return maxHeight
   
  if node.leftnode is not None:
    maxHeight = calculateHeight(node.leftnode, actualHeight + 1, maxHeight)
  if node.rightnode is not None:
    maxHeight = calculateHeight(node.rightnode, actualHeight + 1, maxHeight)

  return maxHeight



def calculateBalance(AVLTree):
  # O(n^2) -> podría se O(n)
  calculateBalanceR(AVLTree.root)


def calculateBalanceR(node):
  if node is None:
     return
  calculateBalanceNode(node)
  if node.leftnode is not None:
    calculateBalanceR( node.leftnode)
  if node.rightnode is not None:
    calculateBalanceR( node.rightnode)
  

def calculateBalanceNode(node):
  # O(n^2) -> podría se O(n)
  if node.leftnode is None and node.rightnode is None:
    node.bf = 0
   
  if node.leftnode is not None and node.rightnode is not None:
    node.bf = calculateHeight(node.leftnode, 0 , 0) - calculateHeight(node.rightnode, 0, 0)
  elif node.leftnode is not None:
    node.bf = calculateHeight(node, 0, 0)
  elif node.rightnode is not None:
    node.bf = - calculateHeight(node, 0, 0)



def reBalance(AVLTree):
  calculateBalance(AVLTree)
  reBalanceR(AVLTree, AVLTree.root)

def reBalanceR(AVLTree, currentNode):
  if currentNode is not None:
    reBalanceNode(AVLTree, currentNode)
    reBalanceR(AVLTree, currentNode.leftnode)
    reBalanceR(AVLTree, currentNode.rightnode)


def reBalanceNode(tree,current):
  if current.bf == 2:
     if current.leftnode is not None:
        if current.leftnode.bf == -1:
           print("caso especial")
           rotateLeft(tree, current.leftnode)
     rotateRight(tree, current)
     return
  if current.bf == -2:
    if current.rightnode is not None:
        if current.rightnode.bf == 1:
           print("rotate left node right", current.rightnode.key)
           rotateRight(tree, current.rightnode)
           
    print("rotate left node: ", current.key)
    rotateLeft(tree,current)
    return
  

test = AVLTree()
insert(test, 15, 15)
insert(test, 10, 10)
insert(test, 20, 20)
insert(test, 5, 5)
insert(test, 12, 12)
insert(test, 11, 11)
insert(test, 14, 14)

printBTK(test.root)


print("post rotation")
reBalance(test)
printBTK(test.root)