
a, b = map(int, input().strip().split(' '))
star=''
for x in range(b):
    for y in range(a):
        star+='*'
    star+='\n'
print(star)

# 미련하게 품.. 
# answer = ('*'*a +'\n')*b 이런 간단한 방법이 있었네