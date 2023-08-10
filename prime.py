x = int(input(":"))
y = x**(1/2)
for i in range(2,y):
    if x%i == 0 :
        print("not prime")
    else :
        print("prime")