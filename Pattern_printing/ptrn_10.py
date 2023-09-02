# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
x = int(input(":"))
for i in range(x):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(x+1,2*x):
    for j in range(2*x-i):
        print("*",end="")
    print()
