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

# QUESTÃO 6
# Implemente um deque através de duas pilhas. 
# Não crie variáveis, use apenas as operações das pilhas e não use recursão.
class Deque:
    def __init__(self, capacity):
        self.frontStack = Stack(capacity)
        self.backStack = Stack(capacity)

    def push_front(self, data):
        # Inserir na frente → empilha direto em frontStack
        self.frontStack.push(data)

    def push_back(self, data):
        # Inserir no fim → empilha direto em backStack
        self.backStack.push(data)

    def pop_front(self):
        # Se frontStack está vazio, move tudo de backStack pra frontStack
        if self.frontStack.isEmpty():
            while not self.backStack.isEmpty():
                self.frontStack.push(self.backStack.pop())

        if self.frontStack.isEmpty():
            print("Deque Underflow (vazio na frente)")
            return None
        return self.frontStack.pop()

    def pop_back(self):
        # Se backStack está vazio, move tudo de frontStack pra backStack
        if self.backStack.isEmpty():
            while not self.frontStack.isEmpty():
                self.backStack.push(self.frontStack.pop())

        if self.backStack.isEmpty():
            print("Deque Underflow (vazio atrás)")
            return None
        return self.backStack.pop()

    def peek_front(self):
        # Garante que o elemento da frente esteja em frontStack
        if self.frontStack.isEmpty():
            while not self.backStack.isEmpty():
                self.frontStack.push(self.backStack.pop())

        if self.frontStack.isEmpty():
            print("Deque vazio (peek_front)")
            return None
        return self.frontStack.peek()

    def peek_back(self):
        # Garante que o elemento de trás esteja em backStack
        if self.backStack.isEmpty():
            while not self.frontStack.isEmpty():
                self.backStack.push(self.frontStack.pop())

        if self.backStack.isEmpty():
            print("Deque vazio (peek_back)")
            return None
        return self.backStack.peek()

    def isEmpty(self):
        return self.frontStack.isEmpty() and self.backStack.isEmpty()

# QUESTÃO 7
# Implemente uma pilha usando filas.
class StackUsingQueues:
    def __init__(self, limit=5):
        self.q1 = Queue(limit)
        self.q2 = Queue(limit)
        self.limit = limit

    def push(self, item):
        self.q2.enQueue(item)

        while not self.q1.isEmpty():
            self.q2.enQueue(self.q1.deQueue())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.isEmpty():
            print("Stack Underflow")
            return None
        return self.q1.deQueue()

    def peek(self):
        if self.q1.isEmpty():
            print("Stack vazia")
            return None
        return self.q1.que[self.q1.front] 

    def isEmpty(self):
        return self.q1.isEmpty()

    def size(self):
        return self.q1.size

# QUESTÃO 8
# Inverta os primeiros k elementos de uma fila.
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