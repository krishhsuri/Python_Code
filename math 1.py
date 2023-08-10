x = int(input("Enter The Base Number :"))
n = int(input("Enter The Power Number :"))
total = 1
for i in range (1 , n+1):
    total += pow(x,i)
print(total)

