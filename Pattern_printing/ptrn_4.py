# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
x = int(input(":"))
for i in range(0,x):
    for j in range(1,i+2):
        print(j,end=" ")
    print()