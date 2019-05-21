# move all zeroes to the end
# o(n) time complexity
 
    def moveZeroes(self, arr):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 # Count of non-zero elements 
        n = len(arr)
        # Traverse the array. If element  
        # encountered is non-zero, then 
        # replace the element at index 
        # 'count' with this element 
        for i in range(n): 
            if arr[i] != 0: 
                # here count is incremented 
                arr[count] = arr[i] 
                count+=1
      
        # Now all non-zero elements have been 
        # shifted to front and 'count' is set 
        # as index of first 0. Make all  
        # elements 0 from count to end. 
        while count < n: 
            arr[count] = 0
            count += 1            
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
