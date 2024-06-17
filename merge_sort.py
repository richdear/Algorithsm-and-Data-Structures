def merge(list1, list2):
    index1=0
    index2=0
    sorted_list=[]
    while index1<len(list1) and index2<len(list2):
        if list1[index1]<list2[index2]:
            sorted_list.append(list1[index1])
            index1+=1
        elif list1[index1]>list2[index2]:
            sorted_list.append(list2[index2])
            index2+=1
        else:
            sorted_list.append(list1[index1])
            sorted_list.append(list2[index2])
            index1+=1
            index2+=1
   
    while index1<len(list1):
        sorted_list.append(list1[index1])
        index1+=1
    
    while index2<len(list2):
        sorted_list.append(list2[index2])
        index2+=1
    
    return sorted_list
    
def sort(items):
    middle=len(items)//2
    list1=items[:middle]
    list2=items[middle:]
    if len(items)==1 or len(items)==0:
        return items
    elif (len(list1)==1 or len(list1)==0) and (len(list2)==0 or len(list2)==1):
        return merge(list1,list2)
    return merge(sort(list1),sort(list2))

# print(merge([3,9,11,19],[1,2,7,10,16]))
# print(merge([19,20,29,41],[18,21,30,39,45]))

print(sort([3,19,77,16,19,1,2,7,10,16]))
print(sort([11,29,21,45,18,46,1,-1,0]))
