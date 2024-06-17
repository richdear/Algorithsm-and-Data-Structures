def bubble_sort(items):
    sorted_items=0

    while sorted_items<len(items):
        for index in range(len(items)-1-sorted_items):
            if items[index]>items[index+1]:
                temp=items[index]
                items[index]=items[index+1]
                items[index+1]=temp
        sorted_items+=1
    return items

def bubble_sort_from_video(items):
    for i in range(len(items)-1,-1,-1):
        for j in range(i):
            if items[j]>items[j+1]:
                temp=items[j]
                items[j]=items[j+1]
                items[j+1]=temp
    return items

#optimize when sorting is done but there are iterations remaining
def bubble_sort_from_video_optimized(items):
    for i in range(len(items)-1,-1,-1):
        any_swaps_last_time=False
        for j in range(i):
            if items[j]>items[j+1]:
               items[j], items[j+1]=items[j+1],items[j]
               any_swaps_last_time=True
        if not any_swaps_last_time:
            break
    return items

print(bubble_sort([3,1,7,16,0,-1,2,46,22,11]))
print(bubble_sort_from_video([3,1,7,16,0,-1,2,46,22,11]))
print(bubble_sort_from_video_optimized([3,1,7,16,0,-1,2,46,22,11]))