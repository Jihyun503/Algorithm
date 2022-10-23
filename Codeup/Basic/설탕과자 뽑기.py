a = []
h, w = map(int, input().split())
n = int(input())

for _ in range(n):
    a.append(input())
    
answer = [[0]*w for _ in range(h)]


for i in range(n):
    t = a[i].split()
    l = t[0]
    d = t[1]
    x = int(t[2]) - 1 #0부터 시작해야해서
    y = int(t[3]) - 1
    answer[x][y] = 1
    
    for j in range(int(l)):
        if d == '0':
            answer[x][y+j] = 1
        else:
            answer[x+j][y] = 1

for i in answer :
    for j in i:
        print(j,end=" ")
    print()
    