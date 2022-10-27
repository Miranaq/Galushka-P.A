# -- coding: utf-8 --
n=int(input())
fact=1
K=0
for i in range(1,n+1):
    fact=fact*i
    K=K+fact
print(K)