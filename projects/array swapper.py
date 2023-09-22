main_list=[3, 25, 13, 6, 35, 8, 14, 45]
for i in range(len(main_list) - 1):
    if main_list[i + 1] % 5 == 0 :
        main_list[i], main_list[i + 1]= main_list[i + 1], main_list[i]
print(main_list)