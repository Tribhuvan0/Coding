class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicti = {}
        dicti_1 = {}
        stri = ""
        if len(s) != len(t):
            return false
        else:
            for i in range(len(s)):
                dicti[s[i]] = t[i]
                dicti_1[t[i]] = s[i]
        for i in range(len(s)):
            stri += dicti[s[i]]
        return len(dicti) == len(dicti_1) and stri == t
        