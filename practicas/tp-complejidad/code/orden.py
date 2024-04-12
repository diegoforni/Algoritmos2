def swapElements(l, id1, id2):
    l[id1], l[id2] = l[id2], l[id1]


def ordenarEj4(l):
    l.sort()
    length = len(l)
    if length < 3:
        return None
    swapElements(l, 2, length // 2)
    swapElements(l, 0, length - 1)

l = [8, 7, 3, 5, 15]

ordenarEj4(l)
print(l)

