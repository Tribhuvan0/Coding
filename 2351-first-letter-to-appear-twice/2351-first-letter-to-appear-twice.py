class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dicti = defaultdict(list)
        mini = float("inf")
        res = ""
        for i in range(len(s)):
            dicti[s[i]].append(i)
        
        for k,v in dicti.items():
            if len(v) >= 2 and v[1] < mini:
                mini = v[1]
                res = k
        return res
                
            
        