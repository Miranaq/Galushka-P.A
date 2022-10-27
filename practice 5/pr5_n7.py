# -- coding: utf-8 --
a=int(input())
b=int(input())
c=0
while b!=0:
    if b>a:
        c=c+1
    a=b
    b=int(input())
print(c)
