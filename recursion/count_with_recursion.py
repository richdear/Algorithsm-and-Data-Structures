def count_to_zero(n):
    if n<=0:
        print("All done!")
        return;
    print(n)
    count_to_zero(n-1)

count_to_zero(5)