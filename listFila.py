from stack import *
from fila import * 

# Inverter Fila com Pilhas
def inverterFilaComPilha(a:Queue):
    if a.isEmpty():
        return None 
    s = Stack()
    while not a.isEmpty():
        s.push(a.deQueue())
        a.deQueue()
    
    while not s.isEmpty():
        a.enQueue(s.push())

    return a

# Inverter a Pilha com Fila
def inverterPilha(s:Stack):
    if s.isEmpty():
        return None
    q = Queue()

    while not s.isEmpty():
        q.enQueue(s.pop())

    while not q.isEmpty():
        s.push(q.deQueue())

    return s

# Inverter K primeiros elementos de uma Fila
def inverterKEl(q:Queue, k):
    if q.isEmpty():
        return None 
    s = Stack()

    for i in range(k):
        s.push(q.deQueue())
    
    while not s.isEmpty():
        q.enQueue(s.pop())
    
    for i in range(q.size - k):
        q.enQueue(q.deQueue())
    

# Implemente uma Fila usando duas Pilhas (Não sei)
class queueWS(object):
    def __init__(self, s1:Stack, s2:Stack, limit=5):
        pass
    def enQueue(self, data):
        self.s1.push(data)
    def deQueue(self):  
        if self.s2.isEmpty():
            while self.s1.isEmpty(): self.s2.push(self.s1.pop())
        return self.s2.pop()


# --------INICIA A LISTA 4---------------

# QUESTÃO 4
# Considere um deque D que contém os números (1,2,3,4,5,6,7,8), nessa ordem. 
# Suponha ainda que há uma fila Q, inicialmente vazia. Elabore um trecho de código que usando 
# apenas D e Q (sem variáveis adicionais) e resulte em Q armazenando os elementos na 
# ordem (1,2,3,4,5,6,7,8).
def transfereDequeParaQueue(D, Q:Queue):
    while not D.isEmpty():
        elem = D.delete_first()
        Q.enQueue(elem)

# QUESTÃO 5
# Implemente uma fila através de duas pilhas. Não crie variáveis, use apenas as operações das 
# pilhas e não use recursão.
class QueueTwoStacks:
    def __init__(self, capacity=10):
        self.S1 = Stack(capacity)
        self.S2 = Stack(capacity)

    def enQueue(self, item):
        while not self.S1.isEmpty():
            self.S2.push(self.S1.pop())

        self.S1.push(item)

        while not self.S2.isEmpty():
            self.S1.push(self.S2.pop())

    def deQueue(self):
        if self.S1.isEmpty():
            print("Fila vazia")
            return None
        return self.S1.pop()
