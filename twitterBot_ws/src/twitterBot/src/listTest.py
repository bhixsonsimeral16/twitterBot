from heapq import *

##on updates from twitter, checks to see if keyword is already in heapq
##if it's in the heap it adds 1 to its value and checks to see if it is more than
##10 above the previous goal
##if the keyword is not in the heap it adds it with a priority of 1
## add prevGoal later
def pulledKeyword(heap, keyword):
    if (len(heap) != 0 and (keyword in (zip(*heap)[1]))):
        #print (heap[zip(*heap)[1].index(keyword)][0])
        heap[zip(*heap)[1].index(keyword)][0] += 1
        #print (heap[zip(*heap)[1].index(keyword)][0])
        # if ((nlargest(1, heap)[1] == keyword) & (heap[zip(*heap)[1].index(keyword)][0]) > (10 + heap[zip(*heap)[1].index(prevGoal)][0])):
        #     ## make a call to change the goal
        #     ## this may be difficult...
        #     ## return is for setting the currentGoal
        #     return (nlargest(1, heap)[1])
    else:
        lst = [1, keyword]
        heappush (heap, lst)
    return heap

## Called when the goal has been reached.  Sets the priority to 0
## Then creates new goal
def goalReached(heap, prevGoal):
    if (prevGoal in (zip(*heap)[1])):
        heap[zip(*heap)[1].index(prevGoal)][0] = 0
        heap.sort
        if ((nlargest(1, heap)[0] > 0)):
            ## make a function call to create a new goal
            ## nlargest(1, heap)[1] is the keyword that becomes the new goal
            ## return is for setting the currentGoal
            return (nlargest(1, heap)[1])
        else:
            ## return is for setting the currentGoal
            ## "stop" is the natural state of the twitterBot
            return("stop")

## currentGoal maintains what the each new goal will be checked against
# currentGoal = "stop"
# priority = []

# l1 = [1, 'forward']
# l2 = [6, 'backward']
# l3 = [3, 'turnRight']
# l4 = [10, 'turnLeft']

# heappush (priority,l1)
# heappush (priority,l2)
# heappush (priority,l3)
# heappush (priority,l4)

#the *priority unzips the heap, so that there are 4 sepearate lists
#instead of whatever they are stored as by the heap
#this does not work with python 3.4, only with 2.7
#zips are not printable or subscriptable in 3.4
#in 3 I will need to add a list() command to change the iterator into a list
# print (priority[list(zip(*priority))[1].index('forward')][0])
#
# priority[list(zip(*priority))[1].index('forward')][0] += 1
#
# print (priority[list(zip(*priority))[1].index('forward')][0])
#
# print (nlargest(4, priority))
#
# while priority:
#     print (heappop(priority))