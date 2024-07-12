class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        stri = ""
        if not s:
            return ""
        for i in range(len(s)):
            #odd length
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    length = r-l+1
                    stri = s[l:r+1]
                
                l -= 1
                r += 1
            
            #even length
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > length:
                    length = r-l+1
                    stri = s[l:r+1]
                
                l -= 1
                r += 1
            
        return stri
        