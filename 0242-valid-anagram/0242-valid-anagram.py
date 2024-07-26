class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i],0)
        for j in range(len(t)):
            tMap[t[j]] = 1 + tMap.get(t[j],0)
        
        return sMap == tMap