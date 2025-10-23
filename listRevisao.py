from stack import * 

# # QUESTÃO 3
# Escreva uma função que verifica se uma string com parênteses e 
# colchetes/chaves ()[]{} está balanceada usando uma pilha
def verificaFechamento(f):
    if f == "":
        return None
    abert = {'{', '[', '('}
    fech = {'}', ']', ')'}
    pares = {')': '(', ']': '[', '}': '{'}
    s = Stack()
    for i in f:
        if i in abert:
            s.push(i)
        if i in fech:
            if s.isEmpty():
                return False
            topo = s.pop()
            if topo != pares[i]:
                return False
            
    return s.isEmpty()