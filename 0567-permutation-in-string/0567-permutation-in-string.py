class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_s1 = {}
        win = len(s1)
        for s in s1:
            hash_s1[s] = 1 + hash_s1.get(s,0)
        
        for i in range(len(s2)):
            if s2[i] in hash_s1:
                hash_s1[s2[i]] -= 1
            
            if i >= win and s2[i-win] in hash_s1:
                hash_s1[s2[i-win]] += 1
            
            if all(hash_s1[i] == 0 for i in hash_s1):
                return True
        return False
        
            
        