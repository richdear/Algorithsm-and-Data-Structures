def frq(text):
    frq={}
    for char in text:
        if char not in frq:
            frq[char]=1
        else:
            frq[char]+=1
    return frq

def anagram(list1, list2):
    if len(list1)!=len(list2):
        return False
    if list1==[] and list2==[]:
        return True
    #count frq of list1
    frq_list1=frq(list1)
    #count freq of list2
    frq_list2=frq(list2)
    #compare frequencies of list1 to list2
    for key1 in frq_list1.keys():
        if key1 not in frq_list2:
            return False
        elif frq_list1[key1]!=frq_list2[key1]:
            return False
    return True

print(anagram('',''))
print(anagram('aaz','zza'))
print(anagram('anagram','nagaram'))
print(anagram('rat','car'))
print(anagram('awesome','awesom'))
print(anagram('qwerty','qeywrt'))
print(anagram('texttwisttime','timetwisttext'))
