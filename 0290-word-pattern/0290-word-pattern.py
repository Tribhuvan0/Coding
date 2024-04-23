class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dicti = {}
        dicti_1 = {}
        str_len  = len(pattern)
        list_s = s.split()
        list_len = len(list_s)
        if list_len != str_len:
            return False
        for i in range(str_len):
            if pattern[i] in dicti and dicti[pattern[i]] != list_s[i]:
                return False
            if list_s[i] in dicti_1 and dicti_1[list_s[i]] != pattern[i]:
                return False
            dicti[pattern[i]] = list_s[i]
            dicti_1[list_s[i]] = pattern[i]
        return True
        