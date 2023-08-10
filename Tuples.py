s = tuple(input("enter values:"))
print(s)
x=0
for i in s:
    print(i)
for j in range(0, len(s)):
    if int(x) > int(s[j]):
        continue
    else:
        x=s[j]
print("The max is:", x)
for j in range(0, len(s)):
    if int(x) < int(s[j]):
        continue
    else:
        x=s[j]
print("The min is:", x)
