def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i

    return f



n=int(input("ENter the value to be factorial:"))
print(fact(n))
