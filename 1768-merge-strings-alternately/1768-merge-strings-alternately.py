class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j = 0,0
        merged = ""
        maxi = max(len(word1), len(word2))
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged += word1[i]
            if j < len(word2):
                merged += word2[j]
            i += 1
            j += 1
        
        return merged
            
        