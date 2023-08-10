s = input("Enter the string :")
word = {"is"}
count = 0
wordslist = list(s.split())
for i in wordslist :
    if i == "is" :
        count += 1
print("Number of *is* is :", count)