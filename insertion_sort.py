def sort(elements):
    length=len(elements)
    for i in range(1,length):
        for j in range(i-1,-1,-1):
            print(f"I :{i} J:{j}")
            print("Before:")
            print(elements)
            if elements[i]<elements[j]:
                temp=elements[i]
                elements[i]=elements[j]
                elements[j]=temp
                i-=1
            print("After:")
            print(elements)
    return elements
nums=[5,2,4,6,1,3]       
print(sort(nums))
