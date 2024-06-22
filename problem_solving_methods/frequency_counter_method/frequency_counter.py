def count_frq(list):
    frq={}
    for item in list:
        if item not in frq:
            frq[item]=1
        else:
            frq[item]+=1
    return frq

def same(list1,list2):
    # count frequency in ar1
    list1_frq=count_frq(list1)
    #count frequency in ar2
    list2_frq=count_frq(list2)
    
    #search for list1->key in list2->keys 
    # if not found return false
    # if found check value
    # if  value dont match return false
    
    for key1 in list1_frq.keys():
        if (key1*key1) not in list2_frq:
            return False
        elif list1_frq[key1]!=list2_frq[key1*key1]:
            return False
    return True

print(same([1,2,3],[4,1,9]))
print(same([1,2,3],[1,9]))
print(same([1,2,1],[4,4,1]))