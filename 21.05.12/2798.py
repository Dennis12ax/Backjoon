
N, M = input().split()
N = int(N)
M = int(M)
card = list(map(int,input().split()))


biggest = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            comb = card[i] + card[j] + card[k]
            if comb >= biggest and M >= comb:
                biggest = comb

print(biggest)
    
