class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
    



class SinglyLinkedList():
    def __init__(self):
        self.length=0
        self.head=None
        self.tail=self.head
    
    def push(self,value):
        if self.head==None:
            self.head=Node(value)
            self.tail=self.head
        else:
            new_node=Node(value)
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    def __str__(self) -> str:
        pointer=self.head
        label=""
        while pointer.next!=None:
            label+=f"{pointer.value} "
            pointer=pointer.next
        label+=f"{pointer.value} "
        return label
    
    def __len__(self):
        return self.length

link_list=SinglyLinkedList()
link_list.push("Teste")
link_list.push("12121")
link_list.push(78)
link_list.push(1)
print(link_list)
print(len(link_list))


