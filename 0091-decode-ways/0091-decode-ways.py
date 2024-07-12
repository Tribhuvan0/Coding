class Solution:
    def numDecodings(self, s: str) -> int:
        #It is n steps approach 2 steps at a time
        if not s:
            return 0
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
    
        for i in range(2,len(s)+1):
            #one digit
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


    def numiDecodings(self, s: str) -> int:
        #it is tree approach pick or not pick type
        
        dicti = {}
        
        def recursiveTree(index):
            if index >= len(s):
                return 1
            if index in dicti:
                return dicti[index]
            if s[index] == '0':
                return 0
            
            #Single digit
            ways = recursiveTree(index+1)
            
            if index + 1 < len(s) and (s[index] == '1' or (s[index] == '2' and s[index+1] in "0123456")):
                ways += recursiveTree(index+2)
                
            dicti[index] = ways
            return ways
        
        return recursiveTree(0)
    

        