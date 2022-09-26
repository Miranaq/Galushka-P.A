# -- coding: utf-8 --
name=input()
age=int(input())
print('Курс Основы программирования начался')
print(16823 * 12302%3092)
if name != 'Иван':
    if 0<age<75:
        if age>=16:
            print('Поздравляем вы поступили в ВГУИТ')
        if age<16:
            print('Сначала нужно окончить школу!')
            print(16-age,'лет учиться')
seconds=int(input())
d=((seconds//86400))
h=((seconds //3600))%24
m=(seconds//60)%60
s=seconds%60
if m<10:
    m=str('0'+str(m))
else:
    m=str(m)
if s<10:
    s=str('0'+str(s))
else:
    s=str(s)
print(str(d)+':'+str(h)+':'+str(m)+':'+str(s))
n=int(input())
print(n + n**2 + n**3 + n**4 + n**5)
x=int(input())
y=int(input())
x,y=y,x
print(x,y)
number=int(input())
if number%2==0:
    print('число чётное')
else:
    print('число нечётное')






