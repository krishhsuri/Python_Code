list = [10,51,2,18,4,31,13,5,23,64,29]
x=0
print("Initial list:","\n",list)
search = int(input("Enter the value to search : "))
val = 0
for i in list :
    if i == search :
        val = 1
        x = list.index(i)

if val == 1:
    print("Element found at index ", x)
else:
    print("Element not found")