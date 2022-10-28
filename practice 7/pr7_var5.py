# -- coding: utf-8 --
n=int(input())
a=[]
b=0
c=1
for i in range(n):
    x=int(input())
    a.append(x)
for i in range(n):
    b=b+a[i]
    c=c+a[i]
print(b)
print(c)