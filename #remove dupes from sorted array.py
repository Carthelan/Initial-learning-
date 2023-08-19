#remove dupes from sorted array
nums = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9]
new_Nums = []
length = 1
for i in range (1, len(nums)):
    if (nums[i] != nums[i - 1]):
        length += 1
        
print(j)