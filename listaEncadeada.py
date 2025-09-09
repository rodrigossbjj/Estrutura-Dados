from linkedList import *

# QUESTÃO 1    
# Dada uma lista simplesmente encadeada que armazena apenas números inteiros, 
# crie uma função em Python que remova todos os números pares. Exemplo L = [1->2->6->13->34->None] 
# Saída L=[1->13->None].

def removePares(h):
    if h == None: return None
    curr = prev = h 
    while curr != None:
        if curr.data%2==0:
            if curr == h:
                prev = h = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return h

# QUESTÃO 2
# Dada uma lista simplesmente encadeada que armazena apenas números inteiros, 
# crie uma função em Python que devolva a soma de todos os números ímpares.
def somaImpares(h):
    if h == None: return None

    curr = h
    soma = 0
    while curr != None:
        if curr.data%2!=0:
            soma += curr.data
        curr.next
    return soma
