def merge_sorted_lists(list1, list2):
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
   
    sorted_list.extend(list1[index1:])
    sorted_list.extend(list2[index2:])
    
    return sorted_list
    
print(merge_sorted_lists([3,9,11,19],[1,2,7,10,16]))
print(merge_sorted_lists([19,20,29,41],[18,21,30,39,45]))
