class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dicti = {}
        for i in text:
            dicti[i] = dicti.get(i,0)+1

        cnt = 0
    
        while dicti.get('b'):
            stri = ''
            if 'b' in dicti and dicti['b'] != 0:
                dicti['b'] -= 1
                stri += 'b'
            if 'a' in dicti and dicti['a'] != 0:
                dicti['a'] -= 1
                stri += 'a'
            if 'l' in dicti and dicti['l'] != 1 and dicti['l'] > 0:
                dicti['l'] -= 2
                stri += 'll'
            if 'o' in dicti and dicti['o'] != 1 and dicti['o'] > 0:
                dicti['o'] -= 2
                stri += 'oo'
            if 'n' in dicti and dicti['n'] != 0:
                dicti['n'] -= 1
                stri += 'n'
            if stri == 'balloon':
                cnt += 1
        return cnt
        