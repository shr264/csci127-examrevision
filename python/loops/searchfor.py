def search(nums, locate):
    found = False
    for i in range(len(nums)):
        print(nums[i])
        if locate == nums[i]:
            found = True
    return(found)
    
nums= [1,4,10,6,5,42,9,8,12]
if search(nums,6):
    print('Found it! 6 is in the list!')
else:
    print('Did not find 6 in the list.')