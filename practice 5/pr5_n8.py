# -- coding: utf-8 --
a=int(input())
b=1
c=0
while a!=0:
    d=int(input())
    a, d= d, a
    if d==a:
        b+=1
    if b>c:
        c=b
    if a!=d:
        b=1
print(c)
