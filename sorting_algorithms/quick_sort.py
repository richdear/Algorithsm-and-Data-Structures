def quick_sort(items):
    if len(items)<=1: return items
    first=items[0]
    small_numbers=0
    for i in range(1,len(items)):
        if items[i]<first:
            small_numbers+=1
            items[small_numbers], items[i] = items[i], items[small_numbers]
    items[0], items[small_numbers] = items[small_numbers], items[0]
    return quick_sort(items[:small_numbers])+[items[small_numbers]]+ quick_sort(items[small_numbers+1:])

def pivot_helper(items):
    first=items[0]
    small_numbers=0
    for i in range(1,len(items)):
        if items[i]<first:
            small_numbers+=1
            items[small_numbers], items[i] = items[i], items[small_numbers]
    items[0], items[small_numbers] = items[small_numbers], items[0]
    return small_numbers

def quick_sort_from_video(items):
    if len(items)<=1: return items
    pivot_index=pivot_helper(items)
    return quick_sort(items[:pivot_index])+[items[pivot_index]]+ quick_sort(items[pivot_index+1:])

items=[5,2,1,8,4,7,6,3]

print(quick_sort(items))

items=[5,2,1,8,4,7,6,3]
pivot_helper(items)
print(items)

items=[5,2,1,8,4,7,6,3]

print(quick_sort_from_video(items))