from stack import *

# QUESTÃO 3
# Implemente uma função que transfira os dados de uma pilha S para uma pilha T, de tal forma que
# o topo da pilha S seja o primeiro elemento da pilha T, e o último elemento de S seja o topo da pilha T
def transferePilha(s:Stack):
    if s.isEmpty():
        return False
    t = Stack()
    while not s.isEmpty():
        t.push(s.pop())
    return t


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

# QUESTÃO 6
# Seja P uma pilha de inteiros não negativos ocupando um array A com N posições, de modo que:
# Números empilhados em P ocupam posições crescentes de A a partir de A[1]
# A[0] contém o índice em A do número empilhado por último (topo da pilha)
# A pilha pode crescer enquanto houver posições em A.
# Implemente as funções de acesso às pilhas: push, pop, peek, len, isEmpty, isFull, empty( esvazia a pilha).
N = 6 
def init():
    A = [0] * N  
    A[0] = 0     
    return A

def isEmpty(A):
    return A[0] == 0

def isFull(A):
    return A[0] == N - 1

def push(A, x):
    if isFull(A):
        print("Erro: pilha cheia!")
        return
    A[0] += 1
    A[A[0]] = x

def pop(A):
    if isEmpty(A):
        print("Erro: pilha vazia!")
        return None
    valor = A[A[0]]
    A[0] -= 1
    return valor

def peek(A):
    if isEmpty(A):
        print("Erro: pilha vazia!")
        return None
    return A[A[0]]

def length(A):
    return A[0]

def empty(A):
    A[0] = 0
