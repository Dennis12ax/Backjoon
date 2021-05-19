
N, K = list(map(int, input().split()))
array = list(range(1,N+1))
result = []

index = K-1
while True:
    result.append(array.pop(index))
    if not array:
        break
    index = (index+K-1) % len(array)

print('<', end = "")
for i in range(N):
    if len(result) - 1 != i:
        print('{}, '.format(result[i]), end ='' )
    else:
        print('{}>'.format(result[i]))
