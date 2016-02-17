from heapq import *

priority = []

def addToQueue(value, key):
    heappush(priority, (value, key))

addToQueue(1, 'forward')
addToQueue(6, 'backward')
addToQueue(3, 'turnRight')
addToQueue(10, 'turnLeft')

print (nlargest(1, priority))
