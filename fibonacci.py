def fib(n):
    a=0
    b=1

    if n==1:
        print(1)
    elif n<0:
        print("no negative number allowed")
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)


x=int(input("Enter value of n"))

fib(x)