nums = [1,4,10,6,5,42,9,8,12] 

maxNum = 0
for n in nums:
    print(n, maxNum)
    if n > maxNum:
        maxNum = n
        print('New max is', maxNum)
print('The max is', maxNum)