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
            label+=f"{pointer.value} "
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




