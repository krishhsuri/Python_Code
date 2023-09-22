dic = {}

while True:
    n = input("Enter name :")
    percentage = float(input("Enter percentage :"))
    dic[n] = percentage
    x = input("Do you want to enter more records enter (Yes/ No)")
    if x == "No" or x == "no":
        break

s = input("Enter name which you want to delete :")
del dic[s]
print("Dictionary", dic)