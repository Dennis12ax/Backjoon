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


# for i in range(N):
#     for j in range(i+1,N):
#         if (count[i][1]-count[i][0]) > (count[j][1]-count[j][0]):
#             temp = count[i]
#             count[i] = count[j]
#             count[j] = temp

# print(count)

# for i in range(N):
#     result.append(count[i])

# for i in ragne(N):
#     for j in range(i+1,N):
        


# print(result)
