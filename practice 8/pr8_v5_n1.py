# -- coding: utf-8 --
def function():
    A=int(input())
    B=int(input())
    C=int(input())
    D=int(input())
    e=A//D-B//C
    g =B*D
    a,b=e,g
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    print((e//a)/(g//a))
function()