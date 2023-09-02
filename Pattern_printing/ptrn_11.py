# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1
x = int(input(":"))
pre =1
for i in range(x):
    for j in range(i+1):
        if (i+j) %2 != 0:
            pre = 0
        else :pre=1
        print(pre,end=" ")

    print()
