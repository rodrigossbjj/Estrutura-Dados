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

# QUESTÃO 3
# Crie uma função que dada uma lista simplesmente encadeada, devolva duas listas circulares com 
# metade dos elementos da primeira. Exemplo: L=[1->2->6->13->34->None] Saída: L1=[1->2->]; L2=[6->13->34->].

def quebrarLista(h):
    if h is None or h.next is None:
        return h, None

    slow = h
    fast = h

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    L1_head = h
    L2_head = slow.next
    slow.next = None  

    curr = L1_head
    while curr.next:
        curr = curr.next
    curr.next = L1_head

    curr = L2_head
    while curr.next:
        curr = curr.next
    curr.next = L2_head

    return L1_head, L2_head

# QUESTÃO 4 
# Dada duas listas simplesmente encadeadas, crie uma função em python que as entrelace. 
# Exemplo: L1=[1->2->3->None] L2=[4->5->6->None] Saída: L3=[1->4->2->5->3->6->None].    

def entrelaceListas(h1, h2):
    if h1 == None and h2 == None: 
        return None
    elif h1 == None and h2 != None:
        return h2
    elif h1 != None and h2 == None:
        return h1
    
    curr1 = h1
    curr2 = h2

    while h1 and h2:
        a = curr1.next 
        b = curr2.next 

        curr1.next = curr2
        if a is None:
            break 
        curr2.next = curr1


        curr1 = a
        curr2 = b

    return h1

def main():
    somaImpares()

if __name__ == "__main__":
    main()