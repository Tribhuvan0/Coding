class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            cnt = 0
            s = list(s)
            s.sort()
            t = list(t)
            t.sort()
            for i in range(len(s)):
                if s[i] == t[i]:
                    cnt += 1
            if cnt == len(s):
                return True
        return False