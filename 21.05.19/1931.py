N = int(input())
count = []
for i in range(N):
    count.append(tuple(map(int, input().split())))



count = sorted(count, key = lambda a:a[0])
count = sorted(count, key = lambda a:a[1])
last = 0
cnt = 0

print(count)

for i,j in count:
    if i >= last:
        cnt+=1
        last = j

print(cnt)

