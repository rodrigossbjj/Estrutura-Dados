from stack import *
from fila import * 

# Inverter Fila com Pilhas
def inverterFila(a:Queue):
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