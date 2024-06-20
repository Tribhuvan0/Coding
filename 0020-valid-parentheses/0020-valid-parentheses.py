class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicti = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in dicti:
                if stack and stack[-1] == dicti[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
            
        