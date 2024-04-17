class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while True:
            if i <= len(s) - 1 and j <= len(t) - 1:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                break
        return i == len(s)
        