class Solution:
    def productExceptSelf(self,nums):
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
        
            
        