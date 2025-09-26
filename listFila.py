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