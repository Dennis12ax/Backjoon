import sys

N = int(sys.stdin.readline())
arr1 = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

for i in range(M):
    print(int(arr2[i]in arr1))