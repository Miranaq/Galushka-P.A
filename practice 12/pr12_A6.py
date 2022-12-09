# -- coding: utf-8 --
def func(A): 
    global d ; global k 
    if d == A and k > 0: return print("Yes") 
    if (d < A and d > 1 and A % d== 0): 
        print("No") 
        return  
    elif( d < A and d > 1): 
        d+=1 
        k+=1 
        return func(A) 
 
d = 2 
A = int(input())
k=0 
func(A)
