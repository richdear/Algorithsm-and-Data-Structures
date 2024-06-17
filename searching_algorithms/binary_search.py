def binary_search(items, val):
    start=0
    end=len(items)
    def search(items, start, end, val):
        index=(start+end)//2
        if items[index]==val:
            return index
        elif start==end:
            return -1
        elif items[index]>val:
            end=index-1
        elif items[index]<val:
            start=index+1
        return search(items, start, end, val)
    return search(items, start, end, val)

items=[1,3,4,6,8,9,11,12,15,16,17,18,19]
print(binary_search(items, 15.5))

items=[1,3,4,6,8,9,11,12,15,16,17,18,19]
print(binary_search(items, 15))

items=[1,2,3]
print(binary_search(items, 1.1))
