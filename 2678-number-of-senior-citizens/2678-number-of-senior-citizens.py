class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for det in details:
            if self.checkAge(det):
                cnt += 1
        return cnt
    
    
    def checkAge(self, stri):
        for i in range(len(stri)):
            if stri[i] == 'M' or stri[i] == 'F' or stri[i] == 'O':
                age = stri[(i+1): -2]
                age = int(age)
                if age > 60:
                    return True
        return False
            
        