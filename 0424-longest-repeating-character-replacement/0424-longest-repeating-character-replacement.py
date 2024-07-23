class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_map = {}
        res = 0
        
        for r in range(len(s)):
            
            freq_map[s[r]] = 1 + freq_map.get(s[r], 0)
            
            cell_cnt = r - l + 1
            if cell_cnt - max(freq_map.values()) <= k:
                res = max(res,cell_cnt)
            
            else:
                
                freq_map[s[l]] -= 1
                if freq_map[s[l]] == 0:
                    freq_map.pop(s[l])
                l += 1
        return res
                
        