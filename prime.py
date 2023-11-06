def prime(x):
    f=0
    for i in range(2,x):
        if x%i==0:
            f=1
            break
    if f==0:
         print(x)

for i in range(1,100):
    prime(i)
