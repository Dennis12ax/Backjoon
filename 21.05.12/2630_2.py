N = int(input())
array = []
white_count = 0
black_count = 0
result =[]

for i in range(N): #그래프 저장
    array.append(list(map(int,input().split())))

def div(x, y, num): # 함수
    global white_count,black_count
    check = array[x][y]
    for i in range(x,x+num):
        for j in range(y,y+num):
            if check != array[i][j]:
                div(x,y,num//2)
                div(x,y+num//2, num//2)
                div(x+num//2, y, num//2)
                div(x+num//2, y+num//2, num//2)
                return
    if check == 0:
        white_count += 1
        result.append(0)
    else:
        black_count += 1
        result.append(1)
        

div(0,0,N)
print(white_count)
print(black_count)
print(result.count(0))
            


