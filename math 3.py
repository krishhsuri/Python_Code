x = int(input("Enter The Base Number :"))
n = int(input("Enter The Power Number :"))
total = 0
for i in range(1, n+1):

    if float(i % 2) != 0:
        total += pow(x, i)/i
    else:
        total -= pow(x,i)/i


print(total)