# -- coding: utf-8 --
def function():
    a = int(input())
    m = []
    def f(x):
        m.append(a)
        while str(a) != '0':
            b = int(input())
            if str(b) != '0':
                m.append(a)
                m.append(b)
                naib = max(m)
                f = min(m)
                for i in range(len(m)):
                    if m[i] < naib and m[i] > f:
                        f = m[i]
            else:
                print('2 наибольшее число =',f)
    print(f(a))
function()
