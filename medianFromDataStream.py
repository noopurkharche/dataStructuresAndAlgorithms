from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low = []
        self.high = []
        
    def addNum(self, num: int):
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))
        
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)
obj.addNum(5)
obj.addNum(6)
print(obj.findMedian())
