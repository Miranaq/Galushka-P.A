a=int(input())
for b in range(1,a//2+1):
    if a%b==0:
        print(b,' ',end='',)
print(a)