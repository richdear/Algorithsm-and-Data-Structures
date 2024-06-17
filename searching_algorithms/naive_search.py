def count_sub_string(text, value):
    counter=0
    index=0
    for char in text:
        if char==value[index]:
            index+=1
        else:
            index=0
        
        if index==len(value):
            counter+=1
            index=0
    return counter

print(count_sub_string("harold said haha in Hamburg","haha"))
print(count_sub_string("wowomgzomg","omg"))