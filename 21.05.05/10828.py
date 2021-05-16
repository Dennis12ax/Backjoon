import sys

def push(x):
    stack.append(x)

def pop():
    if(len(stack) == 0):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if(len(stack) == 0):
        return 1
    else:
        return 0

def top():
    if(len(stack) == 0):
        return -1
    else:
        return stack[-1]


N = int(sys.stdin.readline())
stack = []

for i in range(N):
    iput = sys.stdin.readline().split()
    order = iput[0]

    if order == "push":
        push(iput[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())   