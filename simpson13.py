def simpson13(f,a,b,n):
    h=float(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        k=a+i*h
        if i%2==0:
            result=result+2*f(k)
        else:
            result=result+4*f(k)
    result=result*h/3
    return result

def f(x):
    return sin(x)

from math import*
simpson13(f,0,pi,6)
