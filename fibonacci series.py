n=int(input("Enter the no.of terms:"))
print("Fibonacci Series:")
a=0
b=1
print(a,b,end=",")
for i in range(0,n):
    c=a+b
    print(c,end=",")
    a=b
    b=c
print("...")
    
