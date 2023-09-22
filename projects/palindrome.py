num1=int(input("Enter number: "))
temp=num1
reverse=0
while(num1 > 0):
    digit= num1 % 10
    reverse= reverse * 10 + digit
    num1= num1 // 10
if(temp==reverse):
    print("The number is a palindrome")
else:
    print("The number isn't a palindrome")