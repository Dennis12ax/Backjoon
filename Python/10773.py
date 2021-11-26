K = int(input())
cost = []
for i in range(K):
    coin = int(input())
    if coin == 0:
        cost.pop()
    else:
        cost.append(coin)

result = sum(cost)
print(result)