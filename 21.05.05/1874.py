n = int(input())
stack = []
count = 1
result = []
no_state = True

for i in range(n):
    num = int(input())
    
    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1
        

    if(stack[-1] == num):
        stack.pop()
        result.append("-")
    else:
        no_state=False

if no_state == False:
    print("NO")

else:
    for i in result:
        print(i)
