from binTree import * 
import random 

# Geração de árvore binária de forma aleatória
def buildRandomTree(seed, size):
    root = Node(seed)
    bt = BinTree(root)
    i = 1
    while( i < size):
        p = q = root
        number = random.randint(0,size*40)
        while  number != p.data  and q != None:
            p=q
            if number < p.data:
                q = p.left
            else:
                q = p.right
        if number == p.data:
            continue
        elif number < p.data:
            p.setLeft(number)
        else:
            p.setRight(number)
        i+=1
    return bt, root

# Maior valor de um galho
def max_value(root:BinTree):
    if root is None:
        return float('-inf')
    return max(root.data, max_value(root.left), max(max_value(root.right)))