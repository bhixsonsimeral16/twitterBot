from heapq import *


###this code was made useless after we changed from pushing tuples to lists

##turn tuple into list and then edit the priority value
##valueChange is used rather than just adding a constant 1
##in case we end up get multiple tweets at once.
# def changePriority(tupleBefore, valueChange):
#     lst = list(tupleBefore)
#     lst[0] += valueChange
#     tupleAfter = tuple(lst)
#     return(tupleAfter)

###this code may be redundant
##grab a list from the heap
##this allows ease of access to edit it
def obtainList(heap, key):
    listO = heap[zip(*heap)[1].index(key)]
    return listO

priority = []

#only push lists, this makes them easier to edit
heappush (priority,[1, 'forward'])
heappush (priority,[6, 'backward'])
heappush (priority,[3, 'turnRight'])
heappush (priority,[10, 'turnLeft'])

#may be redundant
# myList = obtainTuple(priority, 'forward')

#this returns the priority of forward as an integer
#priority[zip(*priority)[1].index('forward')]
print (priority[zip(*priority)[1].index('forward')][0])

priority[zip(*priority)[1].index('forward')][0] += 1

print (priority[zip(*priority)[1].index('forward')][0])

print (nlargest(4, priority))

while priority:
    print (heappop(priority))
