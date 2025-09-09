class Node:
    def __init__ (self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    #Add getters and setters
    def __str__(self):
        return "Node[Data=%s]" % self.data


class DoublyLL:

    def __init__(self):
        self.length=0
        self.head=None
        self.tail=None

    def insertAtGivenPosition(self, pos, data):
        if self.head==None or pos ==0:
            self.insertAtBeginning(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif pos < self.length:
            curr = self.head
            count = 0
            while curr != None and count < pos:
                curr = curr.next
                count +=1
            newNode = Node(data)
            newNode.next = curr.next
            newNode.prev = curr
            curr.next = newNode
            self.length += 1

    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if(self.head==None):
            self.head = self.tail = newNode
        else:
            newNode.prev=None
            newNode.next=self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

    def insertAtEnd(self,data):
        if (self.head==None):
            self.head = Node(data)
        else:
            current = self.head
            while(current.next!=None):
                current=current.next
            newNode = Node(data)
            newNode.prev = current
            newNode.next = None
            self.length +=1
    def print(self):
      if self.length != 0:
        pos = 0
        current = self.head
        while current != None:
          print("Node %d has value %s"%(pos, current.data))
          pos +=1
          if pos == self.length : return
          current = current.next

