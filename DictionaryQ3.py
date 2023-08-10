dic = {}

while True :
    name = input("Enter name :")
    mobile = float(input("Enter Mobile number :"))
    price = float(input("Enter Price :"))
    product = input("Enter Product :")
    dic[ name] = [mobile , product , price]
    a = input("Do you want to enter more records enter (Yes/ No)")
    if a == "No" or a == "no":
        break

for i in dic :
    print()
    print("Name : " , i )
    print("Phone : ", dic[ i ][ 0 ] , "\t", "Cost : ", dic[ i ][ 1 ] , "\t", "Item : ", dic[ i ][ 2 ])