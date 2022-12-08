# -- coding: utf-8 --
def function():
    a=int(input())
    def f(a):
        b = a
        c = 0
        for i in range(1, b + 1):
            if b % i == 0:
                c = c+1
        return 'YES' if c == 2 else 'NO'
    print(f(a))
function()