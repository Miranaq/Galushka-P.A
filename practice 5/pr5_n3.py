# -- coding: utf-8 --
def function():
    n=int(input())
    i=1
    while (2**i)<=n:
        i=i+1
    print(2**(i-1),i-1)
function()