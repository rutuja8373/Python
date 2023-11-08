def f(x):
    return x**3-2*x-5

a,b=2,3
for i in range(50):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    if f(c)==0:
        break
    elif f(c)*f(a)<0:
        b=c
    else:
        a=c

print('the root is',c)
