class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        win_size = len(needle)
        i = 0
        j = i + len(needle)
        while j <= len(haystack):
            if haystack[i:j] == needle:
                return i
            i += 1
            j += 1
        return -1
