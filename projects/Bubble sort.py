main = [42,29,74,11,65,58]
num = len(main)
print("Initial List :", main)
for x in range(num - 1):
    for i in range(num - x - 1):
        if main[i] > main[i+1]:
            main[i] , main[i+1] = main[i+1], main[i]
print("Final list ", main)