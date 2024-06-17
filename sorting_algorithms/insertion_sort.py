def insertion_sort(items):
    for current_index in range(1,len(items)):
        insert_position=current_index
        for left_index in range(current_index-1,-1,-1):
            if items[current_index]<items[left_index]:
                insert_position=left_index
        
        if insert_position==current_index:
            continue
        item_to_be_inserted=items[current_index]

        for shift_index in range(current_index, insert_position, -1):
            items[shift_index]=items[shift_index-1]
        
        items[insert_position]=item_to_be_inserted
    return items

def insertion_sort_from_video(items):
    for current_index in range(1,len(items)):
        for left_index in range(current_index-1,-1,-1):
            if items[current_index]<items[left_index]:
                items[current_index], items[left_index] = items[left_index], items[current_index]
                current_index=left_index
    return items

def insertion_sort_simpler(items):
    for current_index in range(1,len(items)):
        current_item=items[current_index]
        for left_index in range(current_index-1,-1,-1):
            if items[left_index]>current_item:
                items[left_index+1]=items[left_index]
            elif items[left_index]<current_item:
                items[left_index+1]=current_item
                break
            if left_index==0:
                items[0]=current_item
    return items
    
print(insertion_sort([5,3,1]))
print(insertion_sort([3,1,7,16,0,-1,2,46,22,11]))

print(insertion_sort_from_video([5,3,1]))
print(insertion_sort_from_video([3,1,7,16,0,-1,2,46,22,11]))

print(insertion_sort_simpler([5,3,1]))
print(insertion_sort_simpler([3,1,7,16,0,-1,2,46,22,11]))