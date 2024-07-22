class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        dicti = {}
        for n in hand:
            dicti[n] = 1 + dicti.get(n,0)
        
        minHeap = list(dicti.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]
            
            for i in range(first, first + groupSize):
                if i not in dicti:
                    return False
                
                dicti[i] -= 1
                if dicti[i] == 0:
                    if minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)
        return True