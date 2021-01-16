# Functions and subroutines operate similarly but have one key difference.
# A function is used when a value is returned to the calling routine,
# while a subroutine is used when a desired task is needed, but no value is returned.

#### Routine:  Kind of displaying time function.


#########  Example 1: Starts #########
from collections import deque

dq = deque([1,2,3,4,5])

dq.append(10)
print(dq)   ### Should come like --->  deque([1, 2, 3, 4, 5, 10])
dq.appendleft(11)
print(dq)   ### Should come like --->  deque([11, 1, 2, 3, 4, 5, 10])
dq.pop()
print(dq)  ### Should come like --->  deque([11, 1, 2, 3, 4, 5])
dq.popleft()
print(dq)  ### Should come like --->  deque([1, 2, 3, 4, 5])
poppeditem = dq.pop()
print(poppeditem)  ## Provide popped value
#########  Example 1: Ends #########


#########  Example 2: Starts #########
from collections import deque

dq1 = deque([1,2,3,4,5],maxlen=5)

dq1.append(10)
print(dq1)   ### Should come like --->  deque([2, 3, 4, 5, 10], maxlen=5)
dq1.appendleft(11)
print(dq1)   ### Should come like --->  ddeque([11, 2, 3, 4, 5], maxlen=5)
dq1.pop()
print(dq1)  ### Should come like --->  deque([11, 2, 3, 4], maxlen=5)
dq1.popleft()
print(dq1)  ### Should come like --->  deque([2, 3, 4], maxlen=5)
popitem = dq1.pop()
print(popitem)  ## Provides popped value:  4
#########  Example 2: Ends #########

