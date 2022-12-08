# -- coding: utf-8 --
def function():
    n = int(input())
    a = 1
    b = 0
    c = 0
    d = 0
    for i in range(1,n+1):
        d=a
        a=d+b
        b=d
        c=c+d
    print(c)
function()