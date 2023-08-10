string = input("Enter the string:")
if(string == string[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

NewString = ""
for i in range(0, len(string)):
    if string[i].islower():
            NewString += string[i].upper()
    elif string[i].isupper():
            NewString += string[i].lower()
    else:
            NewString += string[i]
print("String after case conversion : " + NewString)