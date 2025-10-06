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

# QUESTÃO 7
# Considere duas pilhas de inteiros não negativos P1 e P2 ocupando um único array A com N posições, de modo que:
# Números empilhados em P1 ocupam posições crescentes a partir de A[0]
# Números empilhados em P2 ocupam posições decrescentes de A partir de A[N-1]
# t1 contém o índice em A do número empilhado por último em P1
# t2 contém o índice em A do número empilhado por último em P2
# As pilhas podem crescer enquanto houver posições livres
# Implemente as funções de acesso às pilhas: push, pop, peek, len, isEmpty, isFull, empty
N = 10  

def init():
    A = [0] * N
    t1 = -1      
    t2 = N       
    return A, t1, t2

def isFull(t1, t2):
    return t1 + 1 == t2

def isEmptyP1(t1):
    return t1 == -1

def isEmptyP2(t2):
    return t2 == N

def pushP1(A, x, t1, t2):
    if isFull(t1, t2):
        print("Erro: espaço cheio!")
        return t1, t2
    t1 += 1
    A[t1] = x
    return t1, t2

def pushP2(A, x, t1, t2):
    if isFull(t1, t2):
        print("Erro: espaço cheio!")
        return t1, t2
    t2 -= 1
    A[t2] = x
    return t1, t2

def popP1(A, t1):
    if isEmptyP1(t1):
        print("Erro: P1 vazia!")
        return None, t1
    valor = A[t1]
    t1 -= 1
    return valor, t1

def popP2(A, t2):
    if isEmptyP2(t2):
        print("Erro: P2 vazia!")
        return None, t2
    valor = A[t2]
    t2 += 1
    return valor, t2

def peekP1(A, t1):
    if isEmptyP1(t1):
        print("Erro: P1 vazia!")
        return None
    return A[t1]

def peekP2(A, t2):
    if isEmptyP2(t2):
        print("Erro: P2 vazia!")
        return None
    return A[t2]

def lenP1(t1):
    return t1 + 1

def lenP2(t2):
    return N - t2

def emptyP1():
    return -1

def emptyP2():
    return N

# QUESTÃO 8
# Imagine um processador que possui um único registrador e seis instruções.
# 	LD A coloca o operando A no registrador
# 	ST A coloca o conteúdo do registrador na variável A
# 	AD A soma o conteúdo da variável A ao registrador
# 	SB A subtrai o conteúdo do registrador pela variável A
# 	ML A multiplica o conteúdo do registrador pela variável A
# 	DV A divide o conteúdo do registrador pela variável A

# Escreva um programa que aceite uma expressão posfixa contendo operando de uma única letra e os 
# operadores +,-,*, e/, imprima uma sequência de instruções para avaliar a expressão e deixe o 
# resultado no registrador. Use variáveis da forma TEMPn como variáveis temporárias. Por exemplo, 
# usar a expressão posfixa ABC*+DE-/ deverá imprimir o seguinte:

def gerar_codigo_posfixa(expr):
    pilha = Stack(len(expr))
    temp_count = 0
    codigo = []

    def novo_temp():
        nonlocal temp_count
        temp_count += 1
        return f"TEMP{temp_count}"

    for token in expr:
        if token.isalpha():  
            pilha.push(token)
        else:  
            op2 = pilha.pop()
            op1 = pilha.pop()
            temp = novo_temp()

            if token == '+':
                codigo += [f"LD {op1}", f"AD {op2}", f"ST {temp}"]
            elif token == '-':
                codigo += [f"LD {op1}", f"SB {op2}", f"ST {temp}"]
            elif token == '*':
                codigo += [f"LD {op1}", f"ML {op2}", f"ST {temp}"]
            elif token == '/':
                codigo += [f"LD {op1}", f"DV {op2}", f"ST {temp}"]
            else:
                print(f"Operador desconhecido: {token}")
                continue

            pilha.push(temp)

    return codigo
