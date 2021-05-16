N = int(input())
array = []
wh_count = 0
bk_count = 0
line = []

for i in range(N):
    line = []
    line = input().split()
    array.append(line) 

def divi(num, arr): 
    if num == 1:
        if arr[0] == 1:
            bk_count +=1
        else:
            wh_count +=1

    else:
        por_1=[] # 상단 좌측
        por_1=[row[:num//2] for row in arr[:num//2]]

        por_2 = [] # 상단 우측
        por_2 = [row[num//2:] for row in arr[:num//2]]

        por_3 = [] # 하단 좌측
        por_3 = [row[:num//2] for row in arr[num//2:]]

        por_4 = [] # 하단 우측
        por_4 = [row[num//2:] for row in arr[num//2:]]
    
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0

        for i in range(num//2): #상단 좌측
            for j in range(num//2):
                if por_1[i][j] != 1:
                    divi(num//2, por_1) 
                else:
                    count_1 += 1

        for i in range(num//2):
            for j in range(num//2, num): #상단 우측
                if por_2[i][j] != 1:
                    divi(num//2, por_2)
                else:
                    count_2 += 1

        for i in range(num//2, num): # 하단 좌측
            for j in range(num//2):
                if por_3[i][j] != 1:
                    divi(num//2, por_1)
                else:
                    count_3 += 1

        for i in range(num//2, num): # 하단 우측
            for j in range(num//2, num):
                if por_4[i][j] != 1:
                    divi(num//2, por_1) 
                else:
                    count_4 += 1

        if(count_1 == num//2):
            bk_count+=1
        if(count_2 == num//2):
            bk_count+=1
        if(count_3 == num//2):
            bk_count+=1
        if(count_4 == num//2):
            bk_count+=1
            
    

divi(N,array)

     
print(bk_count,wh_count)