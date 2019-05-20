# move all zeroes to the end
# o(n) time complexity

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    res1 = []
    
    # copy no n zero elements to different array
    for i in nums:
        if i != 0:
            res1.append(i)
    
    n=nums.count(0)
    
    for i in range(len(res1)+n):
        if i<len(res1):
            nums[i] = res1[i]
        else:
            nums[i] = 0
            
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
