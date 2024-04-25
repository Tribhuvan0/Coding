class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = []
        num = int(sqrt(c)) + 1
        for i in range(num):
            nums.append(i)
        if c == 2 or c == 1 or c == 0:
            return True
        left, right = 0, len(nums) -1
        while left < right:
            if left*left + right*right > c:
                right -= 1
            elif left*left + right*right < c:
                left -= 1
            elif left*left + right*right == c:
                return True
            
        return False
        