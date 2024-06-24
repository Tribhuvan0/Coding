class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = defaultdict(list)
        for stri in strs:
            count = [0] * 26
            for c in stri:
                count[ord(c) - ord('a')] += 1
            dicti[tuple(count)].append(stri)
        return dicti.values()
    
        