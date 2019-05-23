# maximum subaaray 

nums = [-2,-5,6,-2,-3,1,5,-6]

for i in range(1, len(nums)):
    if nums[i-1] > 0:
        nums[i] = nums[i] + nums[i-1]
print(max(nums))
    
    
