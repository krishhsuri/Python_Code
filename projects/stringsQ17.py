s = input("Enter Your String : ")
vowels = 0
vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for i in s:
    if i in vowels_list:
        vowels += 1
print("No of vowels :" , vowels)