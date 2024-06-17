def sum_zero(items):
    index_left=0
    index_right=len(items)-1
    
    while index_left<index_right:
        sum=items[index_left]+items[index_right]
        if sum>0:
            index_right-=1
        elif sum<0:
            index_left-=1
        elif sum==0:
            return [items[index_left], items[index_right]]
    return False

print(sum_zero([-3,-2,-1,0,1,2,3]))
print(sum_zero([-2,-1,0,1,3]))
print(sum_zero([1,2,3]))