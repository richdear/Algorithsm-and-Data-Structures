def sum_range(n):
    if n==1:
        return 1
    return n+sum_range(n-1)

sum_range(3)