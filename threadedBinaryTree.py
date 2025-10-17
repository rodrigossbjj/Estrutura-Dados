class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        self.rtag = True
        self.ltag = True


class BinTree:
    def __init__(self, root = None):
        self.root =root

    def inOrderSucessor(self, p):
        if p.rtag == False: return p.right
        else:
            pos = p.right
            while pos.ltag == True:
                pos = pos.left
            return pos
    def inOrder(self, root):
        p = self.inOrderSucessor(root)
        while p != root:
            print(p.data)
            p = self.inOrderSucessor(p)

    def preorderSucessor(self, p):
        if p.ltag == True : return p.left
        else:
            pos = p
            while pos.rtag == False:
                pos = pos.right
            return pos.right
       
    def preOrder(self,root):
        p = self.preorderSucessor(root)
        while p!= root:
            print(p.data)
            p = self.preorderSucessor(p)

def testePreOrder():
    dummy = Node(0)
    root = Node(1)
    n1 = Node(5)
    n2 = Node(4)
    n3 = Node(7)
    n4 = Node(9)
    n5 = Node(11)
    n6 = Node(21)
    n7 = Node(8)

def testeInOrder():
    dummy = Node(0)
    root = Node(1)
    n1 = Node(5)
    n2 = Node(2)
    n3 = Node(11)
    n4 = Node(16)
    n5 = Node(31)

    dummy.right = dummy
    dummy.left = root


    root.left = n1
    root.right = n3

   
    n1.left = n2
    n1.right = root
    n1.rtag = False
    n2.left = dummy
    n2.right = n1
    n2.rtag = False
    n2.ltag = False

    n3.left = n4
    n3.right = n5

    n5.right = dummy
    n5.rtag = False
    n5.ltag = False
    n5.left = n3
    n4.ltag = False
    n4.right = n3
    n4.rtag = False

    b = BinTree(root)
    b.inOrder(dummy)

testeInOrder()