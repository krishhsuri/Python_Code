num1 = float (input("Enter First Number :"))
num2 = float (input("Enter Second Number :"))
num3 = float(input("Enter the third number :"))
if num1 > num2 and num1 > num3 :
    print(num1 , "is the largest number")
elif num2 > num1 and num2 > num3 :
      print(num2 , "is the largest number")
else:
    print(num3, "is the largest number")


if num1< num2 and num1 <num3 :
    print(num1 , "is the smallest number")
elif num2 < num1 and num2 < num3 :
    print(num2 , "is the smallest number")
else:
    print(num3 , "is the smallest number")