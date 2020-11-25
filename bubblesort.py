def sorting(nums):
    swap = True
    # The loop will run at least once so that it can run again
    while swap:
        swap = False
        for x in range(len(nums)-1):
            if nums[x] > nums[x+1]:
                nums[x], nums[x+1] = nums[x+1], nums[x]
                swap = True

numberlist = [1,5,3,7,6]

sorting(numberlist)

print(numberlist)