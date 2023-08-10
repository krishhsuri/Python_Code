string = input("Enter Your String : ")
vowels = consonants = uppercase = lowercase = 0
vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
empty_list = [" "]
for i in string:
    if i in vowels_list:
        vowels += 1
    elif(i not in vowels_list and ord(i)>=65 and ord(i)<91 or ord(i)>=97 and ord(i)<123):
        consonants += 1
        if i in empty_list :
            consonants-= 1
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
print("Number of Vowels in this String = ", vowels)
print("Number of Consonants in this String = ", consonants)
print("Number of Uppercase characters in this String = ", uppercase)
print("Number of Lowercase characters in this String = ", lowercase)

