Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def trapezoidal(f,a,b,n):
...     h=float(b-a)/n
...     result=0.5*f(a)+0.5*f(b)
...     for i in range(1,n):
...         result=result+f(a+i*h)
...         result=result*h
...         return result
... 
...     
>>> def f(x):
...     return x**3-5*x+1
... 
>>> trapezoidal(f,0,3,5)
3.1296
