#Diego Forni | Legajo:14329 | mail: d.forni0204@gmail.com


class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None

L = LinkedList()



def printList(L):

  current = L.head
  while current is not None:
    print(current.value)
    current = current.nextNode




def add(L, element):

    new_node = Node()
    new_node.value = element


    if L.head is None:

        L.head = new_node
    else:

        new_node.nextNode = L.head
        L.head = new_node

    return L



##########SEARCH##############
def search(L,element):
  #Devuelve la posición del elemento, o None si no lo encuentra
  position = 0
  
  current = L.head
  

  while current is not None:
    if current.value == element:
      return position
    current = current.nextNode
    position += 1
  return None



######Insert
def insert(L,element,position):
  new_node = Node()
  new_node.value = element
  if position == 0:
    L.head = new_node
    return 0
  
  current = L.head
  i = 0

  while current is not None:
    if i == position - 1:
      #Inserta nodo, y asigna el siguiente
      new_node.nextNode = current.nextNode
      current.nextNode = new_node
      return i + 1
    current = current.nextNode
    i = i + 1    
  return None
      



def delete(L,element):

  if L.head is None:
    return None

  position = 0

  current = L.head
  next = current.nextNode

  while next is not None:
    if next.value == element:
      current.nextNode = next.nextNode
      return position + 1
      
    elif position  == 0 and current.value == element:
      L.head = next
      return position

    
    current = current.nextNode
    next = current.nextNode
    position += 1
  return None





#########################################
def length(L):
  position = 0
  
  current = L.head
  
  while current is not None:
    current = current.nextNode
    position += 1
  return position




#############
def access(L,position):
  i = 0
  
  current = L.head
  

  while current is not None:
    if i == position:
      return current.value
    current = current.nextNode
    i += 1
    
  return None



def update(L,element,position):
  current = L.head
  i = 0


  while current is not None:
    if i == position:
      current.value = element
      return i
    current = current.nextNode
    i = i + 1    
  return None
      
