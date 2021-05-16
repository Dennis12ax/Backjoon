# greedy algorithm
N, K = input().split()
N = int(N)
K = int(K)
coin = 0

cost = []
for i in range(N):
    money_cost = int(input())
    cost.append(money_cost)
# print(cost)

for i in range(N-1,-1, -1):
    if K>=cost[i]:
        co = K // cost[i]
        coin = coin + co 
        K = K % cost[i]

print(coin)

   


    