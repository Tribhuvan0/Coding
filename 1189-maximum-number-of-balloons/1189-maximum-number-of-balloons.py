class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dicti = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i in dicti:
                dicti[i] += 1
        dicti['l'] = dicti['l']//2
        dicti['o'] = dicti['o']//2
        return min(dicti.values())
        