def sorted(ls):
    for i in range(3):
        print(ls)
        for j in range(2):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1], ls[j]
sorted([9,8,1,3])