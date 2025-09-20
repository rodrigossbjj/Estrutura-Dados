from stack import *


# QUESTÃO 3
# Implemente uma função que transfira os dados de uma pilha S para uma pilha T, de tal forma que
# o topo da pilha S seja o primeiro elemento da pilha T, e o último elemento de S seja o topo da pilha T
def transferePilha(s:Stack):
    if s.isEmpty():
        return False
    t = Stack()
    aux = Stack()
    while not s.isEmpty():
        aux.push(s.pop())

    while not aux.isEmpty():
        t.push(aux.pop())
    return s, t


# QUESTÃO 4
# Elabore uma função recursiva que remova todos os elementos de uma pilha.
def limpaPilha(s:Stack):
    if s.isEmpty():
        return "stack vazia"
    s.pop()
    return limpaPilha(s)

# QUESTÃO 5
# Implemente uma função que inverta a ordem dos elementos de um vetor usando uma pilha
def inverteVetor(arr):
    if len(arr) == 0: 
        return False
    s = Stack()
    for i in arr:
        s.push(i)
    arr.clear()
    while not s.isEmpty():
        arr.append(s.pop())
    return arr
