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
        popped=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=popped.prev
            popped.prev=None
            self.tail.next=None
        self.length-=1    
        return popped
    
    def shift(self):
        if self.empty():
            return None
        
        popped=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=popped.next
            popped.next=None
            self.head.prev=None
        self.length-=1
        return popped
    
    def unshift(self, value):
        new_node=Node(value)
        if self.empty():
            self.head=new_node
            self.tail=self.head
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    
    def get(self, position):
        if position<0 or position>=self.length:
            return None 
        if position==0:
            return self.head
        if position==self.length-1:
            return self.tail
        
        middle=self.length//2
        if position<middle:
            looper=self.head
            position_counter=0
            while position_counter!=position:
                looper=looper.next
                position_counter+=1
        else:
            looper=self.tail
            position_counter=self.length-1
            while position_counter!=position:
                looper=looper.prev
                position_counter-=1
        return looper
            

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

print("--------------------Shift-----------------------")            
dlist=DoublyLinkedList()
dlist.push("One").push("Two").push("Three").push("Four")
print(dlist)
print(dlist.shift().value)
print(dlist)

print(dlist.shift().value)
print(dlist)

print(dlist.shift().value)
print(dlist)

print(dlist.shift().value)
print(dlist)

print(dlist.shift())
print(dlist)

print("--------------------Unshift-----------------------")            
dlist=DoublyLinkedList()
dlist.push("One").push("Two").push("Three").push("Four")
print(dlist)
dlist.unshift("Five")
print(dlist)

dlist.unshift("Six")
print(dlist)

dlist.unshift("Seven")
print(dlist)

dlist.unshift("Eight")
print(dlist)

print("-------------------Get-------------------------")
dlist=DoublyLinkedList()
dlist.push("One").push("Two").push("Three").push("Four").push("Five").push("Six").push("Seven").push("Eight")
print(dlist)
print(dlist.get(2).value)
print(dlist.get(0).value)
print(dlist.get(1).value)
print(dlist.get(3).value)
print(dlist.get(4).value)
print(dlist.get(6).value)
print(dlist.get(7).value)
print(dlist.get(8))