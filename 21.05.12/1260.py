from collections import deque

N, M, V = list(map(int,input().split()))

array = [[0 for i in range(N+1)] for j in range(N+1)]
print(array)

for i in range(M):
    line= []
    first, last = input().split()
    first = int(first)
    last = int(last)
    array[first][last] = 1
    array[last][first] = 1

visited = [0 for i in range(N+1)] #DFS
visited_list = [0 for i in range(N+1)] #BFS 

def DFS(V):
    visited[V] = 1
    print(V, end = ' ')
    for i in range(1,N+1):
        if array[V][i] == 1 and visited[i] != 1:
            DFS(i)

def BFS(V):

    
    queue = deque()
    queue.append(V)
    visited_list[V] = 1

    while queue:
        T= queue.popleft()
        print(T, end=' ')
        for i in range(1,N+1):
            if visited_list[i] != 1 and array[T][i] == 1:
                queue.append(i)
                visited_list[i] = 1
    
DFS(V)
print()
BFS(V)
  