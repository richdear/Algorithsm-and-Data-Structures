class Node():
    def __init__(self,value: any):
        self.value: any =value
        self.next: Node| None = None
    
class SinglyLinkedList():
    def __init__(self):
        self.length:int=0
        self.head: Node|None =None
        self.tail: Node|None =self.head
    
    def push(self,value: any):
        new_node=Node(value)
        if self.empty():
            self.head=new_node
            self.tail=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def __str__(self) -> str:
        if self.empty():
            return ""
        pointer:Node=self.head
        label:str=""
        while pointer.next!=None:
            label+=f"{pointer.value}, "
            pointer=pointer.next
        label+=f"{pointer.value} "
        return label
    
    def __len__(self)->int:
        return self.length
    
    def empty(self)->bool:
        return self.length==0
    
    def pop(self)->any:
        popped_value=None
        if self.empty():
            popped_value=None
        else:
            pointer=self.head
            prev=None
            while pointer.next!=None:
                prev=pointer
                pointer=pointer.next
            if hasattr(prev,'next'):
                prev.next=None
            popped_value=pointer.value
            self.tail=prev
            self.length-=1
        
        if self.empty():
            self.head=None
            self.tail=None
            
        return popped_value
    
    def shift(self)->any:
        if self.empty():
            return None
        else:
            shifted_value=self.head.value
            self.head=self.head.next
            self.length-=1
        return shifted_value
    
    def unshift(self,value)->any:
        new_node=Node(value)
        new_node.next=self.head
        if self.empty():
            self.tail=new_node
        self.head=new_node
        self.length+=1
        
    def get(self,position:int):
        position_counter=0
        looper=self.head
        if self.empty() or self.length<=position or position<0:
            return None
        else:
            while position_counter!=position:
                looper=looper.next
                position_counter+=1
        return looper
    
    def set(self,position:int, value:any):
        position_counter=0
        looper=self.head
        if self.empty() or self.length<=position or position<0:
            return None
        else:
            while position_counter!=position:
                looper=looper.next
                position_counter+=1
        looper.value=value
        return looper.value
    
    def insert(self,position:int, value:any):
        if  self.length<position or position<0:
            return None
        else:
            if self.empty() or position==0:
                self.unshift(value)
            elif position==self.length:
                self.push(value)
            else:
                prev=self.get(position-1)
                current=self.get(position)
                new_node=Node(value)
                new_node.next=current
                prev.next=new_node
                self.length+=1
        
print("-----------Push------------------------")
link_list=SinglyLinkedList()
link_list.push("Teste")
print(link_list)
link_list.push("12121")
print(link_list)
link_list.push(78)
print(link_list)
link_list.push(1)
print(link_list)

print("-----------Pop------------------------")
link_list=SinglyLinkedList()
link_list.push("Teste")
link_list.push("12121")
link_list.push(78)
link_list.push(1)

link_list.pop()
print(link_list)
link_list.pop()
print(link_list)
link_list.pop()
print(link_list)
link_list.pop()
print(link_list)

print("-----------Shift------------------------")
link_list=SinglyLinkedList()
link_list.push("Teste")
link_list.push("12121")
link_list.push(78)
link_list.push(1)
link_list.shift()
print(link_list)
link_list.shift()
print(link_list)
link_list.shift()
print(link_list)
link_list.shift()
print(link_list)

print("-----------Unshift------------------------")
link_list=SinglyLinkedList()
link_list.unshift("Teste")
print(link_list)
link_list.unshift("12121")
print(link_list)
link_list.unshift(78)
print(link_list)
link_list.unshift(1)
print(link_list)

print("----------Get-------------------------")
link_list=SinglyLinkedList()
link_list.unshift("Teste")
link_list.unshift("12121")
link_list.unshift(78)
link_list.unshift(1)
print(link_list)
print(link_list.get(2).value)
print(link_list.get(0).value)
print(link_list.get(1).value)
print(link_list.get(3).value)

print("----------Set-------------------------")
link_list=SinglyLinkedList()
link_list.push("Teste")
link_list.push("12121")
link_list.push(78)
link_list.push(1)
print(link_list)
link_list.set(3,"Teste")
print(link_list.get(3).value)
link_list.set(0,"12121")
print(link_list.get(0).value)
link_list.set(1,78)
print(link_list.get(1).value)
link_list.set(2,1)
print(link_list.get(3).value)

print("-----------Insert------------------------")
link_list=SinglyLinkedList()
link_list.push("Teste")
link_list.push("12121")
link_list.push(78)
link_list.push(1)
print(link_list)
link_list.insert(0,"new item1")
print(link_list)
link_list.insert(3,"new item2")
print(link_list)
link_list.insert(2,"new item3")
print(link_list)
link_list.insert(1,"new item4")
print(link_list)
link_list.insert(7,"new item5")
print(link_list)
link_list.insert(9,"new item6")
print(link_list)