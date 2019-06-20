def __init__(self):
    self.freq = collections.defaultdict(int)
    self.maxQueue = []
    self.index = 0
        
def push(self, x):
    """
    :type x: int
    :rtype: void
    """
    self.freq[x] += 1
    heapq.heappush(self.maxQueue, (-self.freq[x], -self.index, x))
    self.index += 1

def pop(self):
    """
    :rtype: int
    """
    x = heapq.heappop(self.maxQueue)[2]
    self.freq[x] -= 1
    return x
