# -- coding: utf-8 --
def f(a):
    if ((a % 4 == 0) and a % 100 != 0) or a % 400 == 0:
        print('Да')
    else:
        print('Нет')
f (int(input()))