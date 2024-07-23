class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        length = 0
        for r in range(len(s)):
            if s[r] not in sets:
                sets.add(s[r])
                length = max(length, r - l + 1)
            else:
                while s[r] in sets:
                    sets.remove(s[l])
                    l += 1
                sets.add(s[r])
        return length
                
                
        