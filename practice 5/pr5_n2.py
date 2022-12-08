# -- coding: utf-8 --
def function():
    n=int(input())
    i=n
    m=0
    while i>1:
        if n%i==0:
            m=i
        i=i-1
    print(m)
function()