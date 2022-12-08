# -- coding: utf-8 --
def function():
    x=10
    a=[]
    b=[]
    for i in range(x):
        a.append(int(input()))
    for i in range(x):
        if i not in b:
            b.append(i)
    print(b)
function()