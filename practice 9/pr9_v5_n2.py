# -- coding: utf-8 --
m=int(input())
n=int(input())
a=[]
d=0
for i in range (m):
    b=[]
    for j in range (n):
        print('введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)

print('исходный массив:')
for i in range (m):
    for j in range (n):
        print(a[i][j], end=' ')
    print()

for i in range (m):
    for j in range(n):
        if min(a[i])%2==0:
            if a[i][j]==min(a[i]):
                a[i][j]=0
                break
        elif a[i][j]==min(a[i]):
            a[i][j] = 1
            break
print('изменённый массив:')
for i in range (m):
    for j in range (n):
        print(a[i][j], end=' ')
    print()