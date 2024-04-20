class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicti = {}
        dicti_1 = {}
        for i in range(len(s)):
            if s[i] in dicti and dicti[s[i]] != t[i]:
                return False
            elif t[i] in dicti_1 and dicti_1[t[i]] != s[i]:
                return False
            dicti[s[i]] = t[i]
            dicti_1[t[i]] = s[i]
        
        return True
        