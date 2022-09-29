# -- coding: utf-8 --
def f(a, b, c ,d):
    if (a + b + c + d) % 2 == 0:
        print('да')
    else:
        print('нет')
f(int(input()), int(input()), int(input()), int(input()))