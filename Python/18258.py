import sys
from collections import deque

def push(x):
    queue.append(x)

def pop():
    if(len(queue) == 0):
        return -1
    else:
        return queue.popleft()

def size():
    return len(queue)

def empty():
    if(len(queue) == 0):
        return 1
    else:
        return 0

def front():
    if(len(queue) == 0):
        return -1
    else:
        return queue[0]

def back():
    if(len(queue) == 0):
        return -1
    else:
        return queue[-1]

queue = deque()
N = int(sys.stdin.readline())
for i in range(N):
    sen = sys.stdin.readline().split()
    order = sen[0]
    
    if(order == "push"):
        push(int(sen[1]))
    elif(order == "pop"):
        print(pop())
    elif(order == "size"):
        print(size())
    elif(order == "empty"):
        print(empty())
    elif(order == "front"):
        print(front())
    elif(order == "back"):
        print(back())


