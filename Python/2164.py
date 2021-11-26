# import sys

# def trash():
#     queue[0:-1] = queue[1:]
#     queue.pop()
#     return queue

# def change():
#     temp = queue[0]
#     queue[0:-1] = queue[1:]
#     queue[-1] = temp
#     return queue

# N = int(sys.stdin.readline())
# queue = []
# for i in range(N):
#     queue.append(i+1)

# while(len(queue)>1):   
#     trash()
#     if(len(queue) > 1):
#         change()
    
# print(queue[0])

import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
for i in range(N):
    queue.append(i+1)

while(len(queue)>1):
    queue.popleft()
    queue.append((queue.popleft()))

print(queue[0])