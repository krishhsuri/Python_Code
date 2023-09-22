x = int(input("Enter The Base Number :"))
n = int(input("Enter The Power Number :"))
total = 0
y = 1
for i in range(1, n+1):
    if(y==1):
        y=y*i
        total += pow(x,i)/y
    elif(i%2==0):
        y = y * i
        total += pow(x, i) / y
    else:
        y = y * i
        total -= pow(x, i) / y
print(total)
