nums = [1, 2, 3, 3, 4, 5, 6, 6, 7]
for i in nums:
    if (i != 1) and (nums[(i - 1)] == i):
        nums.remove(i)
    print(nums)