num1=int(input("Enter the terms :"))
x=0
y=1
if num1<=0:
    print("The requested series is", x)
else:
    print(x, y, end=" ")
    for i in range(2, num1):
        sum= x + y
        print(sum, end=" ")
        x=y
        y=sum