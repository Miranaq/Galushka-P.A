# -- coding: utf-8 --
m=int(input())
n=int(input())
a=[]
for i in range (m):
    b=[]
    for j in range (n):
        print('введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
#сам массив
print('исходный массив:')
for i in range (m):
    for j in range (n):
        print(a[i][j], end=' ')
    print()
for i in range (m):
    a[i].sort()
print(a)