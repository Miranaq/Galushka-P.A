def f(n, m, k):
    if (k % n == 0 or k % m == 0) and (k < n * m):
        print('Да')
    else:
        print('Нет')
f(int(input()), int(input()), int(input()))