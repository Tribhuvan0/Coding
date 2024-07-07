class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stri = ""
        lst = []
        for i in digits:
            stri += str(i)
        num = str(int(stri) + 1)
        
        i = 0
        while i < len(num):
            lst.append(int(num[i]))
            i += 1
        
        return lst
        
        
        