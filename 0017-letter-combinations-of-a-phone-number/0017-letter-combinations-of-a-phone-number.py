class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        combs,curcombs = [],[]
        self.helper(0,digits, digit_to_char,combs,curcombs)
        return combs
    
    def helper(self,i,digits,digit_to_char,combs,curcombs):
        if i == len(digits):
            combs.append("".join(curcombs))
            return
        
        for char in digit_to_char[digits[i]]:
            curcombs.append(char)
            self.helper(i+1,digits,digit_to_char,combs,curcombs)
            curcombs.pop()
        