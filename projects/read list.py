main_list = eval(input("Enter the list :"))
pos_list = []
neg_list = []

for i in main_list :
    if i >= 0 :
        pos_list.append(i)
    else:
        neg_list.append(i)
print("Main List :", main_list)
print("Positive List :", pos_list)
print("Negative List :", neg_list)