from collections import deque

stack = [] # DFS, LIFO
visited = []

N, M, V = list(map(int,input().split()))

for i in range(M):
    first, last = input().split()
    