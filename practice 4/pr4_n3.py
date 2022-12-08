# -*- coding: utf-8 -*-
def function():
    a=int(input())
    b=int(input())
    def f(a,b):
        if a>b:
            for i in range(a, b - 1, -1):
                print(i)
function()