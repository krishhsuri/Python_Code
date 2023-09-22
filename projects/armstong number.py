num = int(input("Enter The Number :"))
length = len(str(num))
total = 0
temp = num
while temp > 0:
   digit = temp % 10
   total += digit ** length
   temp //= 10
if num == total:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
