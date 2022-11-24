from collections import Counter
from collections import deque
import heapq

tasks = ["A", "A", "A", "B", "B", "C", "C"]
n = 2
count = Counter(tasks)
maxHeap = [-cnt for cnt in count.values()]
heapq.heapify(maxHeap)
queue = deque()
time = 0
while maxHeap or queue:
    time += 1
    if maxHeap:
        val = 1 +  heapq.heappop(maxHeap)
    if val:
        queue.append([val, time + n])
    if queue and queue[0][1] == time:
        qVal = queue.popleft()
        heapq.heappush(maxHeap, qVal)
print(time)
