s = eval(input("Enter First tuple :"))
s1 = eval(input("Enter Second tuple :"))

print("First tuple :", s)
print("Second tuple : ", s1)

s, s1 = s1, s

print("After interchanging;", "\n","Tuple1 =", s, "\n", "Tuple 2 =", s1)
print("t1 < t2 =", s < s1)
print("t1 > t2 =", s > s1)
print("t1 ==  t2 =", s == s1)