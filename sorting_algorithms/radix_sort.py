def get_digit(number, position):
    digit=(number%pow(10,position))//pow(10,position-1)
    return digit

def count_digits(number):
    return len(str(number))


def radix_sort(items):
    max=items[0]
    for item in items:
        if item>max:
            max=item
    max_digit_number=count_digits(max)
    
    for digit_number in range(1,max_digit_number+1):
        container=[[] for _ in range(10)]
        for item in items:
            digit=get_digit(item,digit_number)
            container[digit].append(item)
        items=[]
        for container_item in container:
            items.extend(container_item)
    return items

print(get_digit(5679,1))

print(radix_sort([1556,4,3556,408,4386,902,7,8157,86,9637,29]))
