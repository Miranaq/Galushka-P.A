# -*- coding: utf-8 -*-
a=int(input())
b=int(input())
def bolshe(a, b):
    for i in range(a, b + 1, +1):
        print(i)


def menshe(a,b):
    for i in range(a, b - 1, -1):
        print(i)


if a < b:
    bolshe(a,b)
else:
    menshe(a,b)