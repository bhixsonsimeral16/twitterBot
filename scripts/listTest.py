from heapq import *

priority = []

l1 = [1, 'forward']
l2 = [6, 'backward']
l3 = [3, 'turnRight']
l4 = [10, 'turnLeft']

heappush (priority,l1)
heappush (priority,l2)
heappush (priority,l3)
heappush (priority,l4)

print (priority[zip(*priority)[1].index('forward')][0])

priority[zip(*priority)[1].index('forward')][0] += 1

print (priority[zip(*priority)[1].index('forward')][0])

print (nlargest(4, priority))

while priority:
    print (heappop(priority))
