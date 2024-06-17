def selection_sort(items):
    sorted_items=0
    while sorted_items<len(items):
        min_index=sorted_items
        for i in range(sorted_items,len(items)):
            if items[min_index]>items[i]:
                min_index=i
        
        items[sorted_items], items[min_index] = items[min_index], items[sorted_items] 
        sorted_items+=1
    return items

def selection_sort_from_video(items):
    for i in range(len(items)):
        min_index=i
        for j in range(i,len(items)):
            if items[min_index]>items[j]:
                min_index=j
        if min_index!=i:
            items[i], items[min_index] = items[min_index], items[i]
    return items

print(selection_sort([3,1,7,16,0,-1,2,46,22,11]))
print(selection_sort_from_video([3,1,7,16,0,-1,2,46,22,11]))
