n = int(input())
mns = n
hrs = mns // 60
mns = n % 60
if n < 1440:
    print(hrs, mns, sep=':')
else:
    days = hrs // 24
    hrs %= 24
    print(days,':', hrs, ':', mns)