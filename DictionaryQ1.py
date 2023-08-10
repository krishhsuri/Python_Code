
dic = {}

while True :
    x = int(input("Enter class :"))
    t = input("Enter class teacher name :")
    dic[x]= t
    s = input("Do you want to enter more records enter (Yes/ No)")
    if s == "No" or s == "no":
        break

x = int(input("Enter class which you want to search"))
print("class teacher name", dic[x])