class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def push(self,value):
        new_node=Node(value)
        if self.empty():
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return self
        
    def empty(self):
        return self.length==0
    
    def __str__(self):
        label=""
        looper=self.head
        
        while looper!=None:
            label+=f"{looper.value}, "
            looper=looper.next
        return label

    def pop(self):
        if self.empty():
            return None
        elif self.length==1:
            popped=self.tail
            self.head=None
            self.tail=None
            self.length-=1
            return popped
        else:
            popped=self.tail
            self.tail=popped.prev
            popped.prev=None
            self.tail.next=None
            self.length-=1
            return popped

print("--------------------Push-----------------------")            
dlist=DoublyLinkedList()
dlist.push("One").push("Two").push("Three").push("Four")
print(dlist)

print("--------------------Pop-----------------------")            
dlist=DoublyLinkedList()
dlist.push("One").push("Two").push("Three").push("Four")
print(dlist)
print(dlist.pop().value)
print(dlist)

print(dlist.pop().value)
print(dlist)

print(dlist.pop().value)
print(dlist)

print(dlist.pop().value)
print(dlist)

print(dlist.pop())
print(dlist)