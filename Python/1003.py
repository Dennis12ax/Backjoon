T = int(input())

count_0 = [1, 0, 1]
count_1 = [0, 1, 1]

def fibbonaci(x):
    if len(count_0) <= x:
        for i in range(len(count_0), x+1):
            count_0.append(count_0[i-1] + count_0[i-2])
            count_1.append(count_1[i-1] + count_1[i-2])

for i in range(T):
    N = int(input())
    fibbonaci(N)
    print("{0} {1}". format(count_0[N], count_1[N]))