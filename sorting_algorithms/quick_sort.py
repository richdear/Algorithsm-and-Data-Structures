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

def pivot_helper(items, start=0, end=0):
    pivot=items[start]
    small_numbers=start
    for i in range(start+1,end):
        if items[i]<pivot:
            small_numbers+=1
            items[small_numbers], items[i] = items[i], items[small_numbers]
    items[start], items[small_numbers] = items[small_numbers], items[start]
    return small_numbers

def quick_sort_from_video(items, start, end):
    if end-start<=1: return
    pivot_index=pivot_helper(items,start,end)
    start_left=0
    end_left=pivot_index
    quick_sort_from_video(items,start_left,end_left)

    start_right=pivot_index+1
    end_right=end
    quick_sort_from_video(items,start_right,end_right)

# items=[5,2,1,8,4,7,6,3]

# print(quick_sort(items))

# items=[5,2,1,8,4,7,6,3]
# pivot_helper(items,0,len(items))
# items=[3, 2, 1, 4, 5, 7, 6, 8]
# pivot_helper(items,0,4)
# print(items)

items=[5,2,1,8,4,7,6,3]
quick_sort_from_video(items,0,len(items))
print(items)