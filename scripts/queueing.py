from heapq import *

priority = []

##class Element:
##    def __init__(self, key, value):
##        self.key = key
##        self.value = value
##
##    def __eq__(self, other):
##        return self.key == other.key

heappush (priority,(1, 'forward'))
heappush (priority,(6, 'backward'))
heappush (priority,(3, 'turnRight'))
heappush (priority,(10, 'turnLeft'))

print ('forward' in zip(*priority))

print (nlargest(4, priority))

while priority:
    print (heappop(priority))
