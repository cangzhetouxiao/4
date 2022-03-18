for i in range(1, 1001):
    j = i*i - i
    if 1 <= j <= 100000 and j % 100 == 0:
        print(j)
        print(i)
