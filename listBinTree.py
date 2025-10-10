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


# Verificar se existe um valor na árvore
def verificar(r:BinTree, data):
    if r is None:
        return False
    if r.value == data:
        return True
    return verificar(r.left, data) or verificar(r.right, data)

def verificarInterativo(r:BinTree, data):
    if r is None:
        return False 
    q = Queue()
    q.enQueue(r)
    while not q.isEmpty():
        n = q.deQueue()
        if n == data:
            return True
        if n.left:
            q.enQueue(n.left)
        if n.right:
            q.enQueue(n.right)
    return False

# Quantidade de nós
def verificarNósInterativo(r:BinTree):
    if r is None:
        return False 
    s = Stack()
    s.push(r)
    count = 0
    while not s.isEmpty():
        n = s.pop()
        count += 1
        if n.left:
            s.push(n.left)
        if n.right:
            s.push(n.right)
    return count

def verificarNós(r:BinTree):
    if r is None:
        return 0
    return 1 + verificarNós(r.left) + verificarNós(r.right)

# Percurso inverso do em nível
def percusoInverso(r:BinTree):
    if r is None:
        return False 
    q = Queue()
    q1 = Queue()
    q.enQueue(r)
    s = Stack()
    while not q.isEmpty():
        n = q.deQueue()
        q1.enQueue(n)
        if n.left:
            q.enQueue(n.left)
        if n.right:
            q.enQueue(n.right)
    while not q1.isEmpty():
        s.push(q1.deQueue())

    while not s.isEmpty():
        print(s.pop())
    return None

# Altura da árvore
def alturaArvore(r:BinTree):
    if r is None:
        return 0
    q = Queue()
    q.enQueue(r)
    count = 0
    while not q.isEmpty():
        n = q.len()
        for _ in range(n):
            node = q.deQueue()
            if node.left:
                q.enQueue(node.left)
            if node.right:
                q.enQueue(node.right)
        count += 1
    return count

# Maior soma dos niveis
def alturaArvore(r:BinTree):
    if r is None:
        return 0
    q = Queue()
    q.enQueue(r)
    soma = 0
    mS = 0
    while not q.isEmpty():
        n = q.len()
        for _ in range(n):
            node = q.deQueue()
            if node.left:
                q.enQueue(node.left)
            if node.right:
                q.enQueue(node.right)
            soma += n.data 
        if soma > mS:
            mS = soma
    return mS

def main():
    b = buildRandomTree()

if __name__ == "__main__":
    main()