def count_unique_values(items):
    counter=len(items)
    index1=0
    index2=index1+1
    while index2<len(items):
        equals=items[index1]==items[index2]
        # print(f"Index1: {index1} Index2: {index2}")
        if equals:
            counter-=1
            index2+=1
        elif not equals:
            index1=index2
            index2+=1
    return counter

def count_unique_values_sol_from_video(items):
    if items==[]:
        return 0
    index1=0
    index2=index1+1
    while index2<len(items):
        if items[index1]!=items[index2]:
            index1+=1
            items[index1]=items[index2]
        index2+=1
    return index1+1


# print(count_unique_values([1,1,1,1,1,2]))
# print(count_unique_values([1,2,3,4,4,4,7,7,12,12,13]))
# print(count_unique_values([]))
# print(count_unique_values([-2,-1,-1,0,1]))

print(count_unique_values_sol_from_video([1,1,1,1,1,2]))
print(count_unique_values_sol_from_video([1,2,3,4,4,4,7,7,12,12,13]))
print(count_unique_values_sol_from_video([]))
print(count_unique_values_sol_from_video([-2,-1,-1,0,1]))