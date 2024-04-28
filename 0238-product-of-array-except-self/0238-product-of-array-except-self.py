class Solution:
    def productEceptSelf(self,nums):
        #O(n) space complexity
        prefix = []
        postfix = []
        output = []
        
        prod = 1
        for i in range(len(nums)):
            prod = prod*nums[i]
            prefix.append(prod)

        
        produ = 1
        for i in range(len(nums)-1,-1,-1):
            produ = produ*nums[i]
            postfix.append(produ)
        postfix = list(reversed(postfix))
       
        
        proda = 1
        for i in range(len(nums)):
            if i != 0 and i!= len(nums)-1:
                output.append(prefix[i-1]*postfix[i+1])
            elif i == 0:
                output.append(postfix[1])
            else:
                output.append(prefix[-2])
            
        return output
    
    def productExceptSelf(self,nums):
        #O(1) space complexity
        res = [0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
            
        