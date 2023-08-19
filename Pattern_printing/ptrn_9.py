# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15
x = int(input(":"))
y=1
for i in range(x+1):
    if i<5:
        for j in range(i):
            print(y,end="  ")
            y+=1
    else:
        for j in range(i):
            print(y,end=" ")
            y+=1

    print()